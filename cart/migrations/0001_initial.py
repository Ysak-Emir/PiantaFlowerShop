# Generated by Django 4.1.2 on 2022-12-11 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Decorated', 'Decorated'), ('Сanceled', 'Сanceled')], default='New', max_length=20, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество')),
                ('color', models.CharField(max_length=30, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order', verbose_name='Заказ')),
            ],
        ),
    ]