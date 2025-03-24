# Generated by Django 5.1.7 on 2025-03-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('desc', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='products/')),
                ('stock', models.PositiveBigIntegerField()),
            ],
        ),
    ]
