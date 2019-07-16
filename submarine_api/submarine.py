import json
import requests

# SUBMARINE_API = "https://submarineswaps.org/api/v0"
SUBMARINE_API = "http://localhost:9889/api/v0"


def create(network: str, invoice: str, refund:str):
    """POST a new swap
    """
    data = {'network': network,
            'invoice': invoice,
            'refund': refund}
    return requests.post(url=f"{SUBMARINE_API}/swaps/", json=data)


def check_status(network: str, invoice: str, redeem_script: str):
    """POST a swap check request
    """
    data = {'network': network,
            'invoice': invoice,
            'redeem_script': redeem_script}
    return requests.post(url=f"{SUBMARINE_API}/swaps/check", json=data)


def broadcast_tx(network: str, transaction: str):
    """POST a transaction to broadcast to the network
    """
    data = {'network': network,
            'transaction': transaction}
    return requests.post(url=f"{SUBMARINE_API}/transactions/", json=data)


def get_address_details(address: str, network: str):
    """GET details about an address
    """
    params = {'address': address, 'network': network}
    return requests.get(url=f"{SUBMARINE_API}/address_details/{network}/{address}",
                        params=json.dumps(params))


def get_exchange_rates():
    """GET exchange rate information
    """
    return requests.get(url=f"{SUBMARINE_API}/exchange_rates/")


def get_invoice_details(network: str, invoice: str):
    """GET details about an invoice
    """
    params = {'network': network, 'invoice': invoice}
    return requests.get(url=f"{SUBMARINE_API}/invoice_details/{network}/{invoice}",
                        params=json.dumps(params))


def get_active_networks():
    """GET list of supported networks to pay on-chain
    """
    return requests.get(url=f"{SUBMARINE_API}/networks/")
