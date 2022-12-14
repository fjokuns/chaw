# Generated by Django 4.0.6 on 2022-08-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbro', '0007_dish_showcase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_name', models.CharField(max_length=50)),
                ('show_txt', models.CharField(max_length=250)),
                ('show_img', models.ImageField(default='show.jpg', upload_to='showcase')),
            ],
            options={
                'verbose_name': 'showcase',
                'verbose_name_plural': 'showcase',
                'db_table': 'showcase',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='dish',
            name='showcase',
        ),
    ]
