# Generated by Django 2.2.1 on 2019-10-05 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='number',
            field=models.CharField(default=0, max_length=32, verbose_name='订单编号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.IntegerField(default='0', verbose_name='订单状态'),
            preserve_default=False,
        ),
    ]