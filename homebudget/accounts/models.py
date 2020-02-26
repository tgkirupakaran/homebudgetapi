from django.db import models

# Create your models here.


class Account(models.Model):
    typeChoices = (('Self', 'Self'), ('Third Party',
                                      'Third Party'), ('Owned', 'Owned'))
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000)
    type = models.CharField(
        max_length=100, choices=typeChoices, default='Self')
