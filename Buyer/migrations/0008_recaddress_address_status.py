# Generated by Django 2.2.1 on 2019-10-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0007_recaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='recaddress',
            name='address_status',
            field=models.IntegerField(choices=[(1, '默认地址'), (2, '非默认地址')], default=2),
        ),
    ]
