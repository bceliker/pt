# Generated by Django 2.2.2 on 2019-06-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Dogum Tarihi'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], default='Diğer', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(default=0, verbose_name='Telefon'),
            preserve_default=False,
        ),
    ]
