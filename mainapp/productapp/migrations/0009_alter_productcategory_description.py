# Generated by Django 4.0.6 on 2022-07-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0008_genders_product_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, max_length=100, verbose_name='Описание'),
        ),
    ]
