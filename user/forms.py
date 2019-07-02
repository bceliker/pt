from django import forms
import datetime


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    list_of_gender = [('Erkek','Erkek'),('Kadin','Kadin'),]
    list_of_group = [('Uye', 'Uye'), ('Eğitmen', 'Eğitmen'), ('Yönetici', 'Yönetici'), ]
    #username = forms.CharField(max_length=50, label="Kullanıcı Adı")

    first_name = forms.CharField(max_length=50, label="Ad")
    last_name = forms.CharField(max_length=50, label="Soyad")
    password = forms.CharField(max_length=10, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=10, label="Parola doğrula", widget=forms.PasswordInput)
    birthday = forms.DateField(required=False,widget=forms.DateInput(),label="Dogum Tarihi" )
    gender = forms.ChoiceField(choices=list_of_gender,label="Cinsiyet",widget=forms.Select())
    phone_number = forms.IntegerField(label="Telefon",required=True)
    image_profile = forms.FileField(required=False, label="Profil Fotoğrafı")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['gender'].label = False

    def clean(self):
        #username = self.cleaned_data.get("username")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        gender = self.cleaned_data.get("gender")
        birthday = self.cleaned_data.get("birthday")
        phone_number = self.cleaned_data.get("phone_number")
        image_profile = self.cleaned_data.get("image_profile")
        if password and confirm:
            if password != confirm:
                raise forms.ValidationError("Parolalar uyuşmuyor...")
            else:
                pass
        else:
            raise forms.ValidationError("Parola alanları girilmeli...")
        values = {

            "password": password,
            "first_name":first_name,
            "last_name": last_name,
            "gender": gender,
            "birthday": birthday,
            "phone_number":phone_number,
            "image_profile":image_profile
        }
        return values

