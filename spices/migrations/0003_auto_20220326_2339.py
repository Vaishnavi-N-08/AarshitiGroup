# Generated by Django 3.2.8 on 2022-03-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spices', '0002_remove_cart_products_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
