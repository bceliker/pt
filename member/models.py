from django.db import models
from trainer.models import Trainer

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField("auth.user",on_delete=models.CASCADE,verbose_name="Uye")
    def __str__(self):
        return self.user.username

class MemberAssigment(models.Model):
    member = models.ForeignKey("auth.user", on_delete=models.CASCADE, verbose_name="Uye", related_name="asg_member")
    trainer = models.ForeignKey("auth.user", on_delete=models.CASCADE, verbose_name="Eğitmen",related_name="asg_trainer")
    def __str__(self):
        return self.trainer.username +" / "+ self.member.username



class TrainingTransaction(models.Model):
    member = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Uye", related_name="trn_member")
    trainer = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Eğitmen" , related_name="trn_trainer")
    date = models.DateTimeField(verbose_name="Oluşturma Tarihi")
    time = models.IntegerField(verbose_name="Saat")

    note = models.TextField(verbose_name="Açıklama",max_length=500)

    def __str__(self):
        return self.member.username