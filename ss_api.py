import json

import requests

SUBMARINE_API = "https://submarineswaps.org/api/v0"


def handle_res(res):
    return json.loads(res.text)


class Swap:

    def __init__(self, network: str = None, invoice: str = None, refund: str = None):
        self.network = network
        self.invoice = invoice
        self.refund = refund
        self.swap = None
        self.fee_tokens_per_vbyte = None
        self.payment_hash = None
        self.redeem_script = None
        self.swap_amount = None
        self.swap_fee = None
        self.swap_p2wsh_address = None
        self.timeout_block_height = None
        self.swap_status = None
        self.broadcast_tx = None

    def create(self):
        """POST a new swap
        """
        data = {'network': self.network,
                'invoice': self.invoice,
                'refund': self.refund}
        self.swap = requests.post(url=f"{SUBMARINE_API}/swaps/", json=data)
        if self.swap.status_code == 200:
            json_data = json.loads(self.swap.text)
            assert json_data['invoice'] == self.invoice
            assert json_data['refund_address'] == self.refund
            self.fee_tokens_per_vbyte = json_data['fee_tokens_per_vbyte']
            self.payment_hash = json_data['payment_hash']
            self.redeem_script = json_data['redeem_script']
            self.swap_amount = json_data['swap_amount']
            self.swap_fee = json_data['swap_fee']
            self.swap_p2wsh_address = json_data['swap_p2wsh_address']
            self.timeout_block_height = json_data['timeout_block_height']

    def check_status(self):
        """POST a swap check request
        """
        data = {'network': self.network,
                'invoice': self.invoice,
                'redeem_script': self.redeem_script}
        self.swap_status = requests.post(url=f"{SUBMARINE_API}/swaps/check", json=data)

    def broadcast_tx(self, transaction: str):
        """POST a transaction to broadcast to the network
        """
        data = {'network': self.network,
                'transaction': transaction}
        self.broadcast_tx = requests.post(url=f"{SUBMARINE_API}/transactions/", json=data)


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
