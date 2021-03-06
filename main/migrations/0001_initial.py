# Generated by Django 3.0 on 2019-12-14 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('language', models.CharField(max_length=2, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('menu', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('en', models.CharField(max_length=15)),
                ('it', models.CharField(max_length=15)),
                ('es', models.CharField(max_length=15)),
                ('fr', models.CharField(max_length=15)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Locations')),
            ],
        ),
        migrations.CreateModel(
            name='Disclaimers',
            fields=[
                ('disclaimer', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('en', models.CharField(max_length=50)),
                ('it', models.CharField(max_length=50)),
                ('es', models.CharField(max_length=50)),
                ('fr', models.CharField(max_length=50)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Locations')),
            ],
        ),
    ]
