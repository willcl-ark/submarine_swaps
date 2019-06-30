import json

import requests

SUBMARINE_API = "https://submarineswaps.org/api/v0"


def handle_res(res):
    return json.loads(res.text)


class Swap:

    def __init__(self):
        self.error = None
        self.network = None
        self.address = None
        self.address_details = None
        self.exchange_rates = None
        self.invoice_details = None
        self.active_networks = None
        self.new_swap = None

    def get_address_details(self, address, network):
        """GET details about an address
        """
        params = json.dumps({'address': address, 'network': network})
        res = requests.get(url=f"{SUBMARINE_API}/address_details/{network}/{address}",
                           params=params)
        if res.status_code == 200:
            self.address_details = handle_res(res)
            return
        self.error = (res.status_code, res.reason, res.text)

    def get_exchange_rates(self):
        """GET exchange rate information
        """
        res = requests.get(url=f"{SUBMARINE_API}/exchange_rates/")
        if res.status_code == 200:
            return
        self.error = (res.status_code, res.reason, res.text)

    def get_invoice_details(self, network, invoice):
        """GET details about an invoice
        """
        params = json.dumps({'network': network, 'invoice': invoice})
        res = requests.get(url=f"{SUBMARINE_API}/invoice_details/{network}/{invoice}",
                           params=params)
        if res.status_code == 200:
            self.invoice_details = handle_res(res)
            return
        self.error = (res.status_code, res.reason, res.text)

    def get_active_networks(self):
        """GET list of supported networks to pay on-chain
        """
        res = requests.get(url=f"{SUBMARINE_API}/networks/")
        if res.status_code == 200:
            self.active_networks = handle_res(res)
            return
        self.error = (res.status_code, res.reason, res.text)

    def create_swap(self, network, invoice, refund):
        """POST a new swap
        """
        data = json.dumps({'network': network,
                           'invoice': invoice,
                           'refund': refund})
        res = requests.post(url=f"{SUBMARINE_API}/swaps/", data=data)
        if res.status_code == 200:
            self.new_swap = handle_res(res)
            return
        self.error = res

    def check_swap_status(self, invoice, network, redeem_script):
        """POST a swap check request
        """
        data = json.dumps({'network': network,
                           'invoice': invoice,
                           'redeem_script': redeem_script})
        res = requests.post(url=f"{SUBMARINE_API}/swaps/check", data=data)
        if res.status_code == 200:
            self.new_swap = handle_res(res)
            return
        self.error = res

    def broadcast_transaction(self, network, transaction):
        """POST a transaction to broadcast to the network
        """
        data = json.dumps({'network': network,
                           'transaction': transaction})
        res = requests.post(url=f"{SUBMARINE_API}/transactions/", data=data)
        if res.status_code == 200:
            self.new_swap = handle_res(res)
            return
        self.error = res

