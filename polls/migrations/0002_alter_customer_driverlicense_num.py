# Generated by Django 5.0.2 on 2024-02-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='driverlicense_num',
            field=models.CharField(max_length=50),
        ),
    ]
