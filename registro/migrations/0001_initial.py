# Generated by Django 4.2.7 on 2023-11-20 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
    ]
