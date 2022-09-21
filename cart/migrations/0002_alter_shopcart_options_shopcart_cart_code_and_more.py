# Generated by Django 4.0.6 on 2022-08-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopcart',
            options={'managed': True, 'verbose_name': 'Shopcart', 'verbose_name_plural': 'Shopcart'},
        ),
        migrations.AddField(
            model_name='shopcart',
            name='cart_code',
            field=models.CharField(default='a', max_length=255),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterModelTable(
            name='shopcart',
            table='Shopcart',
        ),
    ]
