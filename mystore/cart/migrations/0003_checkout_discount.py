# Generated by Django 5.0.7 on 2024-09-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='discount',
            field=models.IntegerField(null=True),
        ),
    ]
