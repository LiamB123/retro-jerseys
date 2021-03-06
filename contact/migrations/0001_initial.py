# Generated by Django 2.0.2 on 2019-11-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=300)),
                ('contact', models.EmailField(max_length=80)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='sales_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=300)),
                ('contact', models.EmailField(max_length=80)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='img/received')),
            ],
        ),
    ]
