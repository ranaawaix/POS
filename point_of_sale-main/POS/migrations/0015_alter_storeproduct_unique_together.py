# Generated by Django 3.2.22 on 2023-10-31 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_product_quantity'),
        ('POS', '0014_auto_20231031_0227'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='storeproduct',
            unique_together={('product', 'store')},
        ),
    ]