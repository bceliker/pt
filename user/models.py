from django.db import models
from django.contrib.auth.models import User
from member.models import Member
from trainer.models import Trainer

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    list_of_group = [('Uye', 'Uye'), ('Eğitmen', 'Eğitmen'), ('Yönetici', 'Yönetici'),]
    list_of_gender = [('Erkek', 'Erkek'), ('Kadın', 'Kadın'), ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_grup = models.CharField(max_length=10,choices=list_of_group,default='Uye')

    gender = models.CharField(max_length=10, choices=list_of_gender, default='Diğer')
    phone_number = models.IntegerField(verbose_name="Telefon", blank=False,default=0)
    birthday = models.DateField(verbose_name="Dogum Tarihi",blank=True, null=True)
    image_profile = models.FileField(blank=True, null=True,upload_to='member_profile_image',verbose_name="Fotoğraf Ekleyin")
    def __str__(self):
        return self.user.username
# Profile Table Create
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
