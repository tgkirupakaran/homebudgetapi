from django.db import models
from accounts.models import Account
from categories.models import Category
# Create your models here.


class Transaction(models.Model):
    typeChoices = (('Credit', 'Credit'), ('Debit',
                                          'Debit'))

    amount = models.BigIntegerField()
    type = models.CharField(
        max_length=100, choices=typeChoices, default='Debit')
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    txndate = models.DateTimeField()
    description = models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)
