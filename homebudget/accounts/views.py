from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers import AccountSerializer
from accounts.models import Account
from rest_framework.permissions import IsAuthenticated


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
