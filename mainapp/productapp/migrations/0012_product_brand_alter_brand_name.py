# Generated by Django 4.0.6 on 2022-08-11 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0011_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='productapp.brand'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(default=None, max_length=50, unique=True, verbose_name='Бренд'),
        ),
    ]