# Generated by Django 5.0 on 2023-12-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potter', '0006_spells_alter_elixirs_identifier_alter_houses_animal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spells',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
