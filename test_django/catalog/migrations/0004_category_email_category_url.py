# Generated by Django 4.2.7 on 2023-11-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.URLField(blank=True, verbose_name='url'),
        ),
    ]
