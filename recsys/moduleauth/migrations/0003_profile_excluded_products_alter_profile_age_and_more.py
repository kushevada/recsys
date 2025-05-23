# Generated by Django 5.2 on 2025-04-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduleauth', '0002_profile_age_profile_calorie_adjustment_profile_goal_and_more'),
        ('modulerec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='excluded_products',
            field=models.ManyToManyField(blank=True, related_name='excluded_by_profiles', to='modulerec.product'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(default=18, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='goal',
            field=models.CharField(choices=[('gain', 'Набор'), ('lose', 'Похудение'), ('main', 'Поддержание')], default='maintain', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.PositiveIntegerField(default=160, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.PositiveIntegerField(default=60, verbose_name='Weight'),
        ),
    ]
