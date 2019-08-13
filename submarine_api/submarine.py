import json
import requests

SUBMARINE_API = "https://submarineswaps.org/api/v0"
# SUBMARINE_API = "http://localhost:9889/api/v0"


def get_quote(network, invoice, refund):
    """POST a new swap
    """
    data = {"network": network, "invoice": invoice, "refund": refund}
    return requests.post(url="{}/swaps/".format(SUBMARINE_API), json=data, timeout=30)


def check_status(network, invoice, redeem_script):
    """POST a swap check request
    """
    data = {"network": network, "invoice": invoice, "redeem_script": redeem_script}
    return requests.post(
        url="{}/swaps/check".format(SUBMARINE_API), json=data, timeout=30
    )


def broadcast_tx(network, transaction):
    """POST a transaction to broadcast to the network
    """
    data = {"network": network, "transaction": transaction}
    return requests.post(
        url="{}/transactions/".format(SUBMARINE_API), json=data, timeout=30
    )


def get_address_details(address, network):
    """GET details about an address
    """
    params = {"address": address, "network": network}
    return requests.get(
        url="{}/address_details/{}/{}".format(SUBMARINE_API, network, address),
        params=json.dumps(params),
        timeout=30,
    )


def get_exchange_rates():
    """GET exchange rate information
    """
    return requests.get(url="{}/exchange_rates/".format(SUBMARINE_API), timeout=30)


def get_invoice_details(network, invoice):
    """GET details about an invoice
    """
    params = {"network": network, "invoice": invoice}
    return requests.get(
        url="{}/invoice_details/{}/{}".format(SUBMARINE_API, network, invoice),
        params=json.dumps(params),
        timeout=30,
    )


def get_active_networks():
    """GET list of supported networks to pay on-chain
    """
    return requests.get(url="{}/networks/".format(SUBMARINE_API), timeout=30)
