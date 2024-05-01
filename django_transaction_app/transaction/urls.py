from rest_framework import routers

from .views import TransactionViewSet, WalletViewSet

router = routers.DefaultRouter()
router.register(r"transactions", TransactionViewSet, "transactions")
router.register(r"wallets", WalletViewSet, "wallets")
