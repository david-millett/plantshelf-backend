# Generated by Django 4.2.16 on 2024-11-14 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        ('plants', '0002_plant_bio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='My_plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=40)),
                ('height', models.PositiveIntegerField()),
                ('photo', models.CharField(max_length=200)),
                ('last_watered', models.DateField(blank=True, null=True)),
                ('added_on', models.DateField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contains', to='locations.location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_collection', to=settings.AUTH_USER_MODEL)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individual_plants', to='plants.plant')),
            ],
        ),
    ]