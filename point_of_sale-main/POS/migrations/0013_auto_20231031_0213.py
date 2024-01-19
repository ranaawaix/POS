# Generated by Django 3.2.22 on 2023-10-31 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('POS', '0012_auto_20231030_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cities_light.city'),
        ),
        migrations.AlterField(
            model_name='store',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cities_light.country'),
        ),
    ]