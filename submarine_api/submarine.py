import json
import requests

# SUBMARINE_API = "https://submarineswaps.org/api/v0"
# SUBMARINE_API = "http://localhost:9889/api/v0"


def get_quote(url: str, network: str, invoice: str, refund: str):
    """POST a new swap
    """
    data = {"network": network, "invoice": invoice, "refund": refund}
    return requests.post(url=f"{url}/swaps/", json=data, timeout=30)


def check_status(url: str, network: str, invoice: str, redeem_script: str):
    """POST a swap check request
    """
    data = {"network": network, "invoice": invoice, "redeem_script": redeem_script}
    return requests.post(url=f"{url}/swaps/check", json=data, timeout=30)


def broadcast_tx(url: str, network: str, transaction: str):
    """POST a transaction to broadcast to the network
    """
    data = {"network": network, "transaction": transaction}
    return requests.post(url=f"{url}/transactions/", json=data, timeout=30)


def get_address_details(url: str, address: str, network: str):
    """GET details about an address
    """
    params = {"address": address, "network": network}
    return requests.get(
        url=f"{url}/address_details/{network}/{address}",
        params=json.dumps(params),
        timeout=30,
    )


def get_exchange_rates(url: str, ):
    """GET exchange rate information
    """
    return requests.get(url=f"{url}/exchange_rates/", timeout=30)


def get_invoice_details(url: str, network: str, invoice: str):
    """GET details about an invoice
    """
    params = {"network": network, "invoice": invoice}
    return requests.get(
        url=f"{url}/invoice_details/{network}/{invoice}",
        params=json.dumps(params),
        timeout=30,
    )


def get_active_networks(url: str, ):
    """GET list of supported networks to pay on-chain
    """
    return requests.get(url=f"{url}/networks/", timeout=30)
