# Generated by Django 3.2.22 on 2023-10-30 16:49

from django.db import migrations


def create_initial_data(apps, schema_editor):
    Customer = apps.get_model('POS', 'Customer')
    data = [{"name": "Rodolphe Elner"}, {"name": "Bartlett Neames"}, {"name": "Nikolia Fell"},
            {"name": "Agna Christiensen"}, {"name": "Bron Titley"}, {"name": "Salomo Hargraves"},
            {"name": "Jsandye Facchini"}, {"name": "Willyt Critchell"}, {"name": "Anne-corinne Izhaky"},
            {"name": "Gail Ciccetti"}, {"name": "Melba Pywell"}, {"name": "Peterus Ions"}, {"name": "Sashenka Wards"},
            {"name": "Tawsha Leggat"}, {"name": "Con Wheatman"}, {"name": "Luisa Barradell"}, {"name": "Isadora Hacon"},
            {"name": "Madelena Chasle"}, {"name": "Marylynne Stubbin"}, {"name": "Audry Scawen"},
            {"name": "Charlie Leslie"}, {"name": "Dennie Cadore"}, {"name": "Herschel Dawltrey"},
            {"name": "Catina Skoughman"}, {"name": "Minerva Diggle"}]

    for item in data:
        name = item['name']

        Customer.objects.create(name=name)


class Migration(migrations.Migration):
    dependencies = [('POS', '0002_auto_20231027_1538'), ]

    operations = [
        migrations.RunPython(create_initial_data)
    ]
