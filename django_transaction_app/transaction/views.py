from rest_framework import filters, mixins, viewsets

from .models import Transaction, Wallet
from .serializers import TransactionSerializer, WalletSerializer
from .services import WalletService


class GetPostViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass


class TransactionViewSet(GetPostViewSet):
    """
    API endpoint that allows fetch and add transactions.
    """

    queryset = Transaction.objects.all().order_by("-id")
    serializer_class = TransactionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["id", "txid", "wallet_id__label"]
    ordering_fields = ["id", "txid", "amount"]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        wallet_id = serializer.validated_data["wallet_id"].id
        amount = serializer.validated_data["amount"]
        response = super().create(request)
        WalletService.add_money(wallet_id, amount)
        return response


class WalletViewSet(GetPostViewSet):
    """
    API endpoint that allows fetch and add transactions.
    """

    queryset = Wallet.objects.all().order_by("-id")
    serializer_class = WalletSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["id", "label"]
    ordering_fields = ["id", "label"]
