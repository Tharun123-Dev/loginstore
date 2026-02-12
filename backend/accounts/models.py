from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# Auto create profile when user created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
from django.db import models

class Train(models.Model):
    train_number = models.CharField(max_length=10)
    train_name = models.CharField(max_length=100)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.CharField(max_length=10)
    arrival_time = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.train_number} - {self.train_name}"
