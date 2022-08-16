# Generated by Django 4.0.3 on 2022-08-16 06:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_mrentryrecord_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price1',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='order',
            name='price2',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
