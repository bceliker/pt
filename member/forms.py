from django import forms
from .models import Member,TrainingTransaction
from django.contrib.auth.models import User
from django.utils import timezone


class MemberAssigmentForm(forms.ModelForm):
    trainer = forms.ModelChoiceField(queryset=User.objects.all().filter(profile__user_grup="Eğitmen"))
    def clean(self):
        trainer = self.cleaned_data.get("trainer")
        values = {
            "trainer":trainer
        }
        return values


class TrainingTransactionForm(forms.ModelForm):

    class Meta:
        model = TrainingTransaction
        #fields = '__all__'
        fields ={'trainer','date','time','note'}
    list_of_hour ={
            (6,"06:00"),
            (7,"07:00"),
            (8, "08:00"),
            (9, "09:00"),
            (10, "10:00"),
            (11, "11:00"),
            (12, "12:00"),
            (13, "13:00"),
            (14, "14:00"),
            (15, "15:00"),
            (16, "16:00"),
            (17, "17:00"),
            (18, "18:00"),
            (19, "19:00"),
            (20, "20:00"),
            (21, "21:00"),
            (22, "22:00"),
            (23, "23:00"),
            (24, "24:00"),
            (1, "01:00"),
            (2, "02:00"),
            (3, "03:00"),
            (4, "04:00"),
            (5, "05:00"),}
    trainer = forms.ModelChoiceField(queryset=User.objects.all().filter(profile__user_grup="Eğitmen"))
   # member = forms.ModelChoiceField(queryset=User.objects.all().filter(profile__user_grup="Uye"))
    date = forms.DateField(required=True, widget=forms.SelectDateWidget(years=timezone.now().year), label="Tarih")
    time = forms.ChoiceField(choices=list_of_hour,label='Saat')
    note = forms.Textarea()
