# Generated by Django 2.2.1 on 2019-09-25 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Saller', '0005_auto_20190925_1110'),
        ('Buyer', '0002_delete_loginuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=32, unique=True, verbose_name='订单编号')),
                ('order_date', models.DateField(auto_now=True, verbose_name='订单日期')),
                ('order_status', models.IntegerField(verbose_name='订单状态')),
                ('order_total', models.FloatField(verbose_name='订单总价')),
                ('order_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Saller.LoginUser')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_count', models.IntegerField(verbose_name='商品数量')),
                ('goods_tatol_price', models.FloatField(verbose_name='商品小计')),
                ('good_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Saller.Goods', verbose_name='商品表')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buyer.PayOrder', verbose_name='订单表')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Saller.LoginUser', verbose_name='店铺id')),
            ],
        ),
    ]
