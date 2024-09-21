# By default, Django signals are executed synchronously. This means that when a signal is emitted, the handler (receiver) runs immediately and in the same thread as the code that emitted the signal.

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5) 
    print("Signal handler finished")


