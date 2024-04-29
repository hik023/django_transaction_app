from django.db import models


class Wallet(models.Model):
    label = models.CharField("Label", max_length=255)
    balance = models.DecimalField("Balance", max_digits=20, decimal_places=0)

    def __str__(self):
        return self.label


class Transaction(models.Model):
    amount = models.DecimalField("Amount", max_digits=18, decimal_places=0)
    txid = models.CharField("txid", max_length=255, unique=True)
    wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return self.txid
