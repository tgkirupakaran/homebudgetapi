from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('categories.urls')),
    path('', include('transactions.urls')),
    path('', include('users.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
