from decimal import Decimal

from django.db import transaction

from .models import Wallet


class WalletService:
    @staticmethod
    def add_money(wallet_id: int, amount: Decimal) -> None:
        """
        Adds amount of money to wallet
        """
        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(pk=wallet_id)
            wallet.balance += amount
            wallet.save()
