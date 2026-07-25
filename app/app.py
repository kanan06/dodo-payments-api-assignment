import os
import hashlib
import ipaddress
import socket
from urllib.parse import urlparse

import requests
import yaml
from flask import Flask, request, jsonify

app = Flask(__name__)

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")

LEDGER = [
    {"id": "txn_1001", "pan": "4242424242424242", "amount": 4200, "currency": "USD", "status": "captured"},
    {"id": "txn_1002", "pan": "5555555555554444", "amount": 1899, "currency": "EUR", "status": "refunded"},
]


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/tokenize", methods=["POST"])
def tokenize():
    payload = request.get_json(silent=True) or {}
    pan = payload.get("pan", "")
    token = "tok_" + hashlib.sha256(pan.encode()).hexdigest()[:24]
    return jsonify(token=token, last4=pan[-4:])


@app.route("/transactions")
def transactions():
    return jsonify(transactions=LEDGER)


@app.route("/import", methods=["POST"])
def import_config():
    # Patched: yaml.safe_load cannot construct arbitrary Python objects, unlike the
    # default yaml.load, which is what made the original endpoint exploitable for RCE.
    try:
        config = yaml.safe_load(request.data)
    except yaml.YAMLError:
        return jsonify(error="invalid or unsupported YAML"), 400
    return jsonify(loaded=str(config))


_BLOCKED_NETWORKS = [ipaddress.ip_network(n) for n in (
    "127.0.0.0/8",    # loopback
    "10.0.0.0/8",     # RFC1918
    "172.16.0.0/12",  # RFC1918
    "192.168.0.0/16", # RFC1918
    "169.254.0.0/16", # link-local — covers the cloud metadata IP (169.254.169.254)
)]


def _is_blocked_destination(url: str) -> bool:
    host = urlparse(url).hostname
    if not host:
        return True  # no parsable hostname at all — reject rather than guess
    try:
        resolved_ip = ipaddress.ip_address(host)
    except ValueError:
        # Not a bare IP literal — it's a domain name, so resolve it and check the
        # actual IP it points to. NOTE: this is a known-incomplete mitigation against
        # DNS rebinding (the name could re-resolve to a different IP between this
        # check and the actual request) — the durable fix is an egress allowlist
        # enforced at the network layer, which is exactly what the Task 3
        # NetworkPolicy/Istio egress control is for. This app-level check is
        # defense-in-depth on top of that, not a substitute for it.
        try:
            resolved_ip = ipaddress.ip_address(socket.gethostbyname(host))
        except (socket.gaierror, ValueError):
            return True  # couldn't resolve — reject rather than let requests try
    return any(resolved_ip in net for net in _BLOCKED_NETWORKS)


@app.route("/fetch")
def fetch():
    url = request.args.get("url", "")
    if _is_blocked_destination(url):
        return jsonify(error="destination not allowed"), 403
    resp = requests.get(url, timeout=5)
    return jsonify(status_code=resp.status_code, body=resp.text[:2048])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # nosemgrep: python.flask.security.audit.app-run-param-config
    # Justification: required for reachability inside a Kubernetes pod/Service; binding to
    # 127.0.0.1 would make the container unreachable from the Service. Actual network
    # exposure is scoped by the Task 3 NetworkPolicy + Istio AuthorizationPolicy, not by
    # this bind address.
