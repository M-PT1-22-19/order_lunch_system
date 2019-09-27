# Generated by Django 2.2.5 on 2019-09-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата/Время')),
                ('user', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('product', models.TextField(verbose_name='Заказ')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('paid', models.FloatField(verbose_name='Оплачено')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-published'],
            },
        ),
    ]