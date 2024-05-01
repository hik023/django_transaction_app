from random import randint

from django.core.management.base import BaseCommand
from transaction.models import Transaction, Wallet
from transaction.services import WalletService


class Command(BaseCommand):
    help = "Fill database with some data"

    @staticmethod
    def create_transactions_for_wallet(wallet: Wallet, n: int) -> list[Transaction]:
        """
        Create transaction list for bulk create
        """
        rand_part = randint(1, 50000)
        return [
            Transaction(
                wallet_id=wallet,
                txid=f"{i}_{wallet.label}_{rand_part}tx",
                amount=randint(1, 10000),
            )
            for i in range(n)
        ]

    def handle(self, *args, **options):
        wallet_1 = Wallet.objects.create(label="test_1")
        wallet_2 = Wallet.objects.create(label="test_2")

        print("Added 2 wallets")

        transactions_order = [
            (wallet_1, 7),
            (wallet_2, 6),
            (wallet_1, 11),
            (wallet_2, 9),
        ]

        for wallet, transaction_count in transactions_order:
            transactions = self.create_transactions_for_wallet(
                wallet=wallet, n=transaction_count
            )
            amount = sum([t.amount for t in transactions])
            Transaction.objects.bulk_create(transactions)
            WalletService.add_money(wallet_id=wallet.id, amount=amount)

        print("Added 33 transactions")