from django.urls import path
from . import views

app_name = "member"

urlpatterns = [
    path('detail/<int:id>/', views.detail, name = "detail"),
    path('training_detail/<int:id>/', views.training_detail, name="training_detail"),
]
