from rest_framework import routers

from .views import TransactionViewSet, WalletViewSet

router = routers.DefaultRouter()
router.register(r"transactions", TransactionViewSet)
router.register(r"wallets", WalletViewSet)
