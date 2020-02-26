from rest_framework import routers
from .views import TransactionViewSet

router = routers.DefaultRouter()
router.register('api/transactions', TransactionViewSet, 'transactions')

urlpatterns = router.urls
