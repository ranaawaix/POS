# Generated by Django 3.2.23 on 2023-11-20 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('POS', '0038_alter_store_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='user_accounts.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='user_accounts.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='POS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_cash_in_hand', models.IntegerField()),
                ('closing_cash_in_hand', models.IntegerField()),
                ('total_cash', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pos', to='POS.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='saleitem',
            name='register',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='saleitems', to='POS.pos'),
            preserve_default=False,
        ),
    ]
