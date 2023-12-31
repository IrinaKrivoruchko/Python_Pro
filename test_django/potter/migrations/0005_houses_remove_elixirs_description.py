# Generated by Django 5.0 on 2023-12-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potter', '0004_elixirs_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=50, unique=True, verbose_name='identifier')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('houseColours', models.CharField(max_length=50, verbose_name='Name')),
                ('founder', models.CharField(max_length=50, verbose_name='Name')),
                ('animal', models.CharField(max_length=50, verbose_name='Name')),
                ('element', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультети',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='elixirs',
            name='description',
        ),
    ]
