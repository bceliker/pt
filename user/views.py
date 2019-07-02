from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from member.models import Member
from trainer.models import Trainer
from user.models import Profile


@login_required(login_url="user:login")
def register_member(request):
    form = RegisterForm(request.POST or None,request.FILES or None)
    trainers = User.objects.filter(profile__user_grup="Eğitmen")

    print("************************  username:  ", request.POST.get('username'))
    print("************************  password:  ", request.POST.get('password'))
    print("************************  confirm:  ", request.POST.get('confirm'))
    print("************************  first_name:  ", request.POST.get('first_name'))
    print("************************  last_name:  ", request.POST.get('last_name'))
    print("************************  gender:  ", request.POST.get('gender'))
    print("************************  birthday:  ", request.POST.get('birthday'))
    print("************************  phone_number:  ", request.POST.get('phone_number'))
    print("************************  image_profile:  ", request.POST.get('image_profile'))

    if form.is_valid():
        password = form.cleaned_data.get("password")
        first_name = form.cleaned_data.get("first_name").capitalize()
        last_name = form.cleaned_data.get("last_name").capitalize()

        gender = form.cleaned_data.get("gender")
        birthday = form.cleaned_data.get("birthday")
        phone_number = form.cleaned_data.get("phone_number")
        image_profile = form.cleaned_data.get("image_profile")
        username =first_name.lower()+"."+last_name.lower()
        try:
            newUser = User(username=username, first_name=first_name, last_name=last_name)
            newUser.set_password(password)
            newUser.save()

            print("************************ newUser.id", newUser.id)
            newProfile = Profile.objects.get(user_id=newUser.id)
            newProfile.image_profile = image_profile
            newProfile.user_grup = "Uye"
            newProfile.phone_number=phone_number
            newProfile.birthday=birthday
            newProfile.gender = gender
            newProfile.save()

            newMember = Member(user=newUser)
            newMember.save()

            # login(request, newUser)

            #newMember = Member(member=newUser, gender=gender, birthday=birthday, phone_number=phone_number,image_profile=image_profile)
            #newMember.save()

            messages.success(request, 'Kullanıcı başarı ile kayıt edildi.')

            return redirect("user:dashboard")
        except:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Böyle bir kullancı var')
            else:
                raise


    else:

        if request.POST:
            messages.info(request, 'Kullanıcı kayıt edilemedi.')
        context = {
            "form": form
        }
        for x in form:
            print(x.value())
        return render(request, "user/register.html", context=context)


    context = {
        "form": form,
        "user_grup": "Member",
        'trainers':trainers
    }
    return render(request, "user/register.html", context=context)



@login_required(login_url="user:login")
def register_trainer(request):
    form = RegisterForm(request.POST or None,request.FILES or None)
    members = User.objects.filter(profile__user_grup="Uye")
    if form.is_valid():
        password = form.cleaned_data.get("password")
        first_name = form.cleaned_data.get("first_name").capitalize()
        last_name = form.cleaned_data.get("last_name").capitalize()

        gender = form.cleaned_data.get("gender")
        birthday = form.cleaned_data.get("birthday")
        phone_number = form.cleaned_data.get("phone_number")
        image_profile = form.cleaned_data.get("image_profile")
        username =first_name.lower()+"."+last_name.lower()
        try:

            newUser = User(username=username, first_name=first_name, last_name=last_name)
            newUser.set_password(password)
            newUser.save()

            newProfile = Profile.objects.get(user_id=newUser.id)
            newProfile.image_profile = image_profile
            newProfile.user_grup = "Eğitmen"
            newProfile.phone_number=phone_number
            newProfile.birthday=birthday
            newProfile.gender = gender
            newProfile.save()

            newTrainer = Trainer(user=newUser)
            newTrainer.save()

            messages.success(request, 'Kullanıcı başarı ile kayıt edildi.')
            return redirect("user:dashboard")
        except:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Böyle bir kullancı var')
            else:
                raise
    else:

        if request.POST:
            messages.info(request, 'Kullanıcı kayıt edilemedi.')

    context = {
        "form": form,
        "user_grup":"Trainer",
        "members":members
    }
    return render(request, "user/register.html", context=context)

def log_in(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request, "Böyle bir kullanıcı yok veya parola hatalı")
            return render(request,"user/login.html",context=context)
        messages.success(request,"Başarı ile giriş yaptınız")
        login(request,user)
        #return render(request,"trainer/dashboard.html")
        return redirect("user:dashboard")
    return render(request,"user/login.html",context=context)



def log_out(request):
    logout(request)
    messages.success(request,"Sistemden çıkış yaptınız")
    return redirect("user:dashboard")

@login_required(login_url="user:login")
def dashboard(request):
    #x = Member.objects.all().order_by("-id")
    #y = User.objects.exclude(id__in=Member.objects.all().values('member_id'))

    x= User.objects.all().filter(profile__user_grup="Uye").order_by("-id")
    context = {

        "users": x
    }
    return render(request, "trainer/dashboard.html", context=context)


