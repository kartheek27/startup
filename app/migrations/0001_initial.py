# Generated by Django 4.2 on 2024-10-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('state', models.CharField(default='', max_length=100)),
                ('district', models.CharField(default='', max_length=100)),
                ('mandal', models.CharField(default='', max_length=100)),
                ('village', models.CharField(default='', max_length=100)),
                ('pin', models.IntegerField(default=0)),
            ],
        ),
    ]
