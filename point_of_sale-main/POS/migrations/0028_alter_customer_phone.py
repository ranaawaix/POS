# Generated by Django 3.2.23 on 2023-11-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0027_alter_sale_total_payable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
