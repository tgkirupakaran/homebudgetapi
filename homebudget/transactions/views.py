from django.shortcuts import render
from rest_framework import viewsets
from transactions.serializers import TransactionSerializer
from transactions.models import Transaction
from rest_framework.permissions import IsAuthenticated


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
