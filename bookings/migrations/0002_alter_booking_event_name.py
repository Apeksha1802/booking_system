# Generated by Django 5.1.3 on 2024-12-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event_name',
            field=models.CharField(max_length=100),
        ),
    ]
