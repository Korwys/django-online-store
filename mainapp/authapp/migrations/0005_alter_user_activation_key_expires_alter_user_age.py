# Generated by Django 4.0.6 on 2022-07-25 17:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 27, 17, 59, 22, 49081, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, verbose_name='Возраст'),
        ),
    ]
