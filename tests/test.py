
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.builder.transaction_builder import TransactionBuilder, CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction
from time import sleep
import unittest

node_uri = "http://localhost:9000/api/v3"
network_id = 3
vote_dao_address = "cx3f9f66cd7478d8dfa85cdf977965000e97bedcba"
keystore_path = "./keystore_test1"
keystore_pw = "test1_Account"

class TestGetterMethods(unittest.TestCase):

    def setUp(self):
        self.wallet = KeyWallet.load(keystore_path, keystore_pw)
        self.tester_addr = self.wallet.get_address()
        self.icon_service = IconService(HTTPProvider(node_uri))

    def test_vote_list(self):
        call = CallBuilder().from_(self.tester_addr)\
                    .to(vote_dao_address)\
                    .method("vote_list")\
                    .build()
        self.icon_service.call(call)

    def test_add_user(self):
        send = CallTransactionBuilder().from_(self.tester_addr) \
            .version(3) \
            .step_limit(3000000000000000000000) \
            .timestamp(0x573117f1d6568) \
            .nid(0x3) \
            .to(vote_dao_address) \
            .method("add_user") \
            .params({"contents": "hx8d29ac2645805452a6e921c888b23c58be862cf0"}) \
            .build()
        signed_transaction = SignedTransaction(send, self.wallet)
        tx_hash = self.icon_service.send_transaction(signed_transaction)

        sleep(10)
        result = self.icon_service.get_transaction_result(tx_hash)
        assert result['status'] == 0 or 1

    def test_remove_user(self):
        send = CallTransactionBuilder().from_(self.tester_addr) \
            .version(3) \
            .step_limit(3000000000000000000000) \
            .timestamp(0x573117f1d6568) \
            .nid(0x3) \
            .to(vote_dao_address) \
            .method("remove_user") \
            .params({"contents": "hx8d29ac2645805452a6e921c888b23c58be862cf0"}) \
            .build()
        signed_transaction = SignedTransaction(send, self.wallet)
        tx_hash = self.icon_service.send_transaction(signed_transaction)

        sleep(10)
        result = self.icon_service.get_transaction_result(tx_hash)
        assert result['status'] == 0 or 1

    def test_ox(self):
        send = CallTransactionBuilder().from_(self.tester_addr) \
            .version(3) \
            .step_limit(3000000000000000000000) \
            .timestamp(0x573117f1d6568) \
            .nid(0x3) \
            .to(vote_dao_address) \
            .method("ox") \
            .params({"contents": "tests"}) \
            .build()
        signed_transaction = SignedTransaction(send, self.wallet)
        tx_hash = self.icon_service.send_transaction(signed_transaction)

        sleep(10)
        result = self.icon_service.get_transaction_result(tx_hash)
        assert result['status'] == 0 or 1

    def vote(self):
        send = CallTransactionBuilder().from_(self.tester_addr) \
            .version(3) \
            .step_limit(3000000000000000000000) \
            .timestamp(0x573117f1d6568) \
            .nid(0x3) \
            .to(vote_dao_address) \
            .method("vote") \
            .params({"code": "O0","vote_res": "2"}) \
            .build()
        signed_transaction = SignedTransaction(send, self.wallet)
        tx_hash = self.icon_service.send_transaction(signed_transaction)

        sleep(10)
        result = self.icon_service.get_transaction_result(tx_hash)
        assert result['status'] == 0 or 1

    def delete(self):
        send = CallTransactionBuilder().from_(self.tester_addr) \
            .version(3) \
            .step_limit(3000000000000000000000) \
            .timestamp(0x573117f1d6568) \
            .nid(0x3) \
            .to(vote_dao_address) \
            .method("delete") \
            .params({"code": "O0"}) \
            .build()
        signed_transaction = SignedTransaction(send, self.wallet)
        tx_hash = self.icon_service.send_transaction(signed_transaction)

        sleep(10)
        result = self.icon_service.get_transaction_result(tx_hash)
        assert result['status'] == 0 or 1


if __name__ == '__main__':
    unittest.main()
