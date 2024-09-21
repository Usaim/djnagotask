#Yes, by default, Django signals run in the same database transaction as the caller if the signal is emitted within a transaction block. 

from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal handler: Current object name is", instance.name)


>>> from myapp.models import MyModel
>>> from django.db import transaction

>>> with transaction.atomic():
...     obj = MyModel.objects.create(name="Object In Transaction")
...     print("Transaction: Current object name is", obj.name)
Transaction: Current object name is Object In Transaction
Signal handler: Current object name is Object In Transaction
