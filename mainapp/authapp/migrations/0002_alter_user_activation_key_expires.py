# Generated by Django 4.0.6 on 2022-07-25 17:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 27, 17, 40, 40, 119431, tzinfo=utc)),
        ),
    ]