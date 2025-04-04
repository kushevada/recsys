from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    height = models.PositiveIntegerField(User, null=False, blank=True, verbose_name='Рост', min_value=120, max_value=300, length=3)
    weight = models.PositiveIntegerField(User, null=False, blank=True, verbose_name='Вес', min_value=25, max_value=500, min_length=2, max_length=3)

def UpdateInfo(self, *args, **kwargs):
    if self.pk:
        updated = Profile.objects.get(pk=self.pk)
        
    super().save(*args, **kwargs)

def __str__(self):
    return f"{self.user}"