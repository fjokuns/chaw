# Generated by Django 4.0.6 on 2022-08-03 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techbro', '0002_alter_category_options_alter_dish_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='techbro.category'),
        ),
    ]
