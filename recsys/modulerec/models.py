from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    ru_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.ru_name if self.ru_name else self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    caloricity = models.FloatField(default=0)
    is_for_weight_main = models.BooleanField(default=False)
    is_for_weight_gain = models.BooleanField(default=False)
    is_for_weight_loss = models.BooleanField(default=False)

    class Meta:
        unique_together = ['name', 'category']

    def __str__(self):
        return self.name

