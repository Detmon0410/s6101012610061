# Generated by Django 3.0.3 on 2020-02-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_GET', '0002_auto_20200226_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculate_log',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
