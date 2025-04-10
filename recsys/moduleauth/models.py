from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="Email")
    sex = models.CharField(max_length=6, choices=[('male', 'Мужской'), ('female', 'Женский')], default='male')
    age = models.PositiveIntegerField(blank=True, default=18, verbose_name='Age' )
    height = models.PositiveIntegerField(blank=True, default=160,verbose_name="Height")
    weight = models.PositiveIntegerField(blank=True, default=60, verbose_name="Weight")
    goal = models.CharField(max_length=20, choices=[('gain', 'Набор веса'), ('lose', 'Похудение')], default='maintain')
    calorie_adjustment = models.IntegerField(default=0, verbose_name="Коррекция калорий")

    # расчет базового метаболизма
    def calculate_daily_calories(self):
        if self.sex == 'male':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        return bmr + self.calorie_adjustment

    def save(self, *args, **kwargs):
        if self.height < 120 or self.height > 300:
            raise ValidationError("Значение роста должно находиться между 120 и 300")
        if self.weight < 25 or self.weight > 300:
            raise ValidationError("Значение веса должно находиться между 25 и 300")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}"