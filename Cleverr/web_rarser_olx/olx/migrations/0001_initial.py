# Generated by Django 3.2.6 on 2021-08-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OlxAdvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Заголовок')),
                ('price', models.CharField(max_length=250, verbose_name='Цена')),
                ('published', models.CharField(max_length=250, verbose_name='Дата публикации')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-time_create'],
            },
        ),
    ]