from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    caloricity = models.FloatField(default=0)
    is_fow_weight_main = models.BooleanField(default=False)
    is_for_weight_gain = models.BooleanField(default=False)
    is_for_weight_loss = models.BooleanField(default=False)



    def __str__(self):
        return self.name

