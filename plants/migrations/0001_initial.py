# Generated by Django 4.2.16 on 2024-11-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=40)),
                ('genus', models.CharField(max_length=20)),
                ('species', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=200)),
                ('light', models.CharField(max_length=20)),
                ('is_toxic', models.BooleanField(default=False)),
                ('difficulty', models.CharField(max_length=20)),
                ('water_interval', models.PositiveIntegerField()),
            ],
        ),
    ]