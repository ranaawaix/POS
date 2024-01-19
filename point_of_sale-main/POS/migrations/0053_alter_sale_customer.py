# Generated by Django 4.2.8 on 2024-01-01 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0052_remove_register_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(default=26, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='POS.customer'),
        ),
    ]