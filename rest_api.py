import json

import requests

SUBMARINE_API = "https://submarineswaps.org/api/v0"


def handle_response(response):
    return json.loads(response.text)


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
        pass

    def get_address_details(self, address, network):
        response = requests.get(url=f"{SUBMARINE_API}/address_details/{network}/{address}")
        if response.status_code == 200:
            self.address_details = handle_response(response)
            return
        self.error = (response.status_code, response.reason, response.text)

    def get_exchange_rates(self):
        response = requests.get(url=f"{SUBMARINE_API}/exchange_rates/")
        if response.status_code == 200:
            self.exchange_rates = handle_response(response)
            return
        self.error = (response.status_code, response.reason, response.text)

    def get_invoice_details(self, network, invoice):
        data = {"network": network, "invoice": invoice}
        data_json = json.dumps(data)
        response = requests.get(url=f"{SUBMARINE_API}/invoice_details/{network}/{invoice}",
                                data=data_json)
        if response.status_code == 200:
            self.invoice_details = handle_response(response)
            return
        self.error = (response.status_code, response.reason, response.text)

    def get_active_networks(self):
        response = requests.get(url=f"{SUBMARINE_API}/networks/")
        if response.status_code == 200:
            self.active_networks = handle_response(response)
            return
        self.error = (response.status_code, response.reason, response.text)

    def post_new_swap(self, network, invoice, refund_address):
        data = {"network": network, "invoice": invoice, "refund": refund_address}
        data_json = json.dumps(data)
        response = requests.post(url=f"{SUBMARINE_API}/swaps/", data=data_json)
        if response.status_code == 200:
            self.new_swap = handle_response(response)
            return
        self.error = (response.status_code, response.reason, response.text)
