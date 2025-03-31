from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_for_weight_gain = models.BooleanField(default=False)
    is_for_weight_loss = models.BooleanField(default=False)

    def __str__(self):
        return self.name