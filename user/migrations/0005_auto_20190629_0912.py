# Generated by Django 2.2.2 on 2019-06-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190628_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(default=0, verbose_name='Telefon'),
        ),
    ]