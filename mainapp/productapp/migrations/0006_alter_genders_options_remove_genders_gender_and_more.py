# Generated by Django 4.0.6 on 2022-07-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0005_genders_alter_gallery_product_product_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genders',
            options={'verbose_name': 'Пол', 'verbose_name_plural': 'Пол'},
        ),
        migrations.RemoveField(
            model_name='genders',
            name='gender',
        ),
        migrations.AddField(
            model_name='genders',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='Пол'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='genders',
            table='gender',
        ),
    ]
