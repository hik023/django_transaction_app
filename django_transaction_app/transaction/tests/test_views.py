from rest_framework.test import APITestCase
from transaction.models import Wallet


class TransactionTestCase(APITestCase):
    def setUp(self):
        self.test_wallet = Wallet.objects.create(label="test_wallet")
        self.TRANSACTION_API_URL = "/api/v1/transactions/"

    def test_wallet_update_after_transaction(self):
        """New transactions updates wallet balance"""
        amount = 111111
        response = self.client.post(
            self.TRANSACTION_API_URL,
            {
                "data": {
                    "type": "Transaction",
                    "attributes": {
                        "amount": amount,
                        "txid": "test1",
                        "wallet_id": self.test_wallet.id,
                    },
                }
            },
            format="vnd.api+json",
        )
        assert response.status_code == 201

        response = self.client.post(
            self.TRANSACTION_API_URL,
            {
                "data": {
                    "type": "Transaction",
                    "attributes": {
                        "amount": amount,
                        "txid": "test2",
                        "wallet_id": self.test_wallet.id,
                    },
                }
            },
            format="vnd.api+json",
        )

        assert Wallet.objects.get(pk=self.test_wallet.id).balance == amount * 2
