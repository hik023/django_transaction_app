from rest_framework import serializers

from .models import Transaction, Wallet


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"
        read_only_fields = ("balance",)
