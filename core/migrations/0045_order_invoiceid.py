# Generated by Django 4.0.3 on 2022-08-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_alter_useritem_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoiceid',
            field=models.DateTimeField(null=True),
        ),
    ]
