from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from modulerec.models import Product, Category


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="Email")
    sex = models.CharField(max_length=6, choices=[('male', 'Мужской'), ('female', 'Женский')], default='male')
    age = models.PositiveIntegerField(default=18, verbose_name='Age' )
    height = models.PositiveIntegerField(default=160,verbose_name="Height")
    weight = models.FloatField(default=60.0, verbose_name="Weight")
    goal = models.CharField(max_length=20, choices=[('gain', 'Набор'), ('lose', 'Похудение'), ('main', 'Поддержание')], default='maintain')
    calorie_adjustment = models.IntegerField(default=0, verbose_name="Коррекция калорий")
    excluded_products = models.ManyToManyField(Product, blank=True, related_name='excluded_by_profiles')
    excluded_categories = models.ManyToManyField(Category, blank=True, related_name='excluded_by_profiles')

    # методы для получения русского значения поля
    def get_sex_display(self):
        return dict(self._meta.get_field('sex').choices).get(self.sex)
    
    def get_goal_display(self):
        return dict(self._meta.get_field('goal').choices).get(self.goal)

    # расчет суточной нормы ккал
    def calculate_daily_calories(self):
        if self.sex == 'male':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        
        if self.goal == 'gain':
            adjustment = 500
        elif self.goal == 'lose':
            adjustment = -500
        else:
            adjustment = 0
        return bmr + adjustment + self.calorie_adjustment
    
    # расчет суточной нормы БЖУ
    def calculate_daily_pfc(self):
        if self.goal == 'gain':
            proteins = self.weight * 2.0
            fats = self.weight * 1.0
            carbohydrates = self.weight * 4.0
        elif self.goal == 'lose':
            proteins = self.weight * 2.5
            fats = self.weight * 0.8
            carbohydrates = self.weight * 2.0
        else:
            proteins = self.weight * 1.8
            fats = self.weight * 0.9
            carbohydrates = self.weight * 3.0
        return {
            'proteins': proteins,
            'fats': fats,
            'carbohydrates': carbohydrates,
            'calories': self.calculate_daily_calories()
        }

    def save(self, *args, **kwargs):
        if self.height < 120 or self.height > 300:
            raise ValidationError("Значение роста должно находиться между 120 и 300")
        if self.weight < 25.0 or self.weight > 300.0:
            raise ValidationError("Значение веса должно находиться между 25 и 300")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}"
    
class WeightHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='weight_history')
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()
