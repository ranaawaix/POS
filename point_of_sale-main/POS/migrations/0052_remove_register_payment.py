# Generated by Django 3.2.23 on 2023-12-08 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0051_register_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='payment',
        ),
    ]
