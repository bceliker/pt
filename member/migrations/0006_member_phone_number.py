# Generated by Django 2.2.2 on 2019-06-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20190614_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(default='05326722783', max_length=12, verbose_name='Telefon'),
            preserve_default=False,
        ),
    ]
