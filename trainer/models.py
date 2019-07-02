from django.db import models

class Trainer(models.Model):
    user = models.OneToOneField("auth.user",on_delete=models.CASCADE,verbose_name="Uye")
    def __str__(self):
        return self.user.username