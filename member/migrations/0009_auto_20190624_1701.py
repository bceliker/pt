# Generated by Django 2.2.2 on 2019-06-24 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20190620_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image_profile',
            field=models.FileField(blank=True, null=True, upload_to='member_profile_image', verbose_name='Fotoğraf Ekleyin'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fkmember', to=settings.AUTH_USER_MODEL, verbose_name='Uye'),
        ),
    ]