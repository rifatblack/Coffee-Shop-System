# Generated by Django 2.1.2 on 2021-09-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FoodInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('can_order', 'Can order the drinks'), ('can_serve', 'Can prepare and serve the drinks')),
            },
        ),
        migrations.CreateModel(
            name='OrderInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('coffee_order', models.CharField(max_length=100)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]