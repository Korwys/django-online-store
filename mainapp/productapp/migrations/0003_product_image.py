# Generated by Django 4.0.6 on 2022-07-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_alter_product_table_alter_productcategory_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=True, upload_to='product_images'),
        ),
    ]
