# Generated by Django 4.0.3 on 2022-11-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_bill_added_bill_customer_returnn_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mother',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
