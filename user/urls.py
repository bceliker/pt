from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/member/',  views.register_member, name = "register_member"),
    path('register/trainer/', views.register_trainer, name = "register_trainer"),
    path('login/', views.log_in, name = "login"),
    path('logout/', views.log_out, name = "logout"),
    path('dashboard/', views.dashboard, name = "dashboard"),
]
