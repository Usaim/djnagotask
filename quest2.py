# Yes, Django signals run in the same thread as the caller by default.

import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")


>>> from myapp.models import MyModel
>>> import threading
>>> print(f"Main code running in thread: {threading.current_thread().name}")
>>> obj = MyModel.objects.create(name="Test Object")
Main code running in thread: MainThread
Signal handler running in thread: MainThread
