# Generated by Django 4.0.6 on 2022-08-11 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0012_product_brand_alter_brand_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
    ]
