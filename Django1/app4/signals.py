from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Book

@receiver(post_save, sender=Book)
def my_function(sender, instance, created, **kwargs):
    if created:
        print(f"New book created:{sender}, {instance.title}")
    else:
        print(f"Book updated: {instance.title}")