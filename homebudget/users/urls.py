from rest_framework import routers
from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/groups', GroupViewSet, 'groups')

urlpatterns = router.urls
