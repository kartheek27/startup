# Generated by Django 4.2 on 2024-10-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mpin',
            field=models.IntegerField(default=0, max_length=6),
        ),
    ]
