# Generated by Django 5.2 on 2025-04-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduleauth', '0003_profile_excluded_products_alter_profile_age_and_more'),
        ('modulerec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='excluded_category',
            field=models.ManyToManyField(blank=True, related_name='categories_excluded_by_profiles', to='modulerec.product'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='excluded_products',
            field=models.ManyToManyField(blank=True, related_name='products_excluded_by_profiles', to='modulerec.product'),
        ),
    ]
