from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from member.forms import TrainingTransactionForm
from django.contrib.auth.models import User
from member.models import TrainingTransaction
from django.contrib import messages
from django.utils import timezone



@login_required(login_url="user:login")
def detail(request,id):
    #art = article.objects.filter(id=id).first()
    #x = Member.objects.all().order_by("-id")
    #y = User.objects.exclude(id__in=Member.objects.all().values('member_id'))

    #member = get_object_or_404(Member,id=id)
    user =get_object_or_404(User,id=id)
    context = {
        "user": user

    }
    return render(request,"member/detail.html",context=context)



@login_required(login_url="user:login")
def training_detail(request,id):
    user =get_object_or_404(User,id=id)
    transaction = TrainingTransaction.objects.filter(member_id=id).order_by("-date","-time")
    trainer = User.objects.all()
    form = TrainingTransactionForm(request.POST or None)

    date = timezone.localtime().now()
    time = range(6,24)
    time_now = timezone.localtime().hour



    context = {
        "form":form,
        "user":user,
        "trainer":trainer,
        "transaction":transaction,
        "date":date,
        "time":time,
        "time_now": time_now
    }



    if form.is_valid():

        new_record = form.save(commit=False)
        new_record.member = User.objects.get(id=id)
        #new_record.date = new_record.date.strftime("%Y-%m-%d")
        #form.member=User.objects.all().filter(id=id).values("id")
        print("Member   ******************************************", new_record.member)
        print("Trainer  ******************************************", new_record.trainer)
        new_record.save()
        messages.success(request,"Kayıt başarı bir şekilde yapıldı")
        return redirect("member:training_detail",id=id)
    return render(request,"member/training_detail.html",context=context)





