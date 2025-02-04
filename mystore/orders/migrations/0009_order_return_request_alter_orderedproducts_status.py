# Generated by Django 5.0.7 on 2024-09-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orderedproducts_payment_status_alter_order_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='return_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderedproducts',
            name='status',
            field=models.CharField(choices=[('Order confirmed', 'Order confirmed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned')], null=True),
        ),
    ]
