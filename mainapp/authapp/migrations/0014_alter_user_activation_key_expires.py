# Generated by Django 4.0.6 on 2022-08-03 04:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 4, 58, 39, 308212, tzinfo=utc)),
        ),
    ]
