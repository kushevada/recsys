# Generated by Django 5.2 on 2025-04-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduleauth', '0004_profile_excluded_category_and_more'),
        ('modulerec', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='excluded_category',
        ),
        migrations.AddField(
            model_name='profile',
            name='excluded_categories',
            field=models.ManyToManyField(blank=True, related_name='excluded_by_profiles', to='modulerec.category'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='excluded_products',
            field=models.ManyToManyField(blank=True, related_name='excluded_by_profiles', to='modulerec.product'),
        ),
    ]
