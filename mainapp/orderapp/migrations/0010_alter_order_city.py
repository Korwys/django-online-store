# Generated by Django 4.0.6 on 2022-08-06 13:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0009_alter_order_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 11', regex='^.{11}$')], verbose_name='Город'),
        ),
    ]
