from django.db import models

# Create your models here.


class Category(models.Model):
    typeChoices = (('Payable', 'Payable'), ('Receivable',
                                            'Receivable'), ('Paid', 'Paid'), ('Recieved', 'Recieved'))
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000)
    type = models.CharField(
        max_length=100, choices=typeChoices, default='Paid')
