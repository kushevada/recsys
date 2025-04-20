from django.db import models
from modulerec.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.value}'