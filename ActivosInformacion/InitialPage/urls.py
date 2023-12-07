from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.enterAsset, name='enterAsset'),
    path('enterUsers/', views.enterUsers, name='enterUsers'),
    path('enterDepartment/', views.enterDepartment, name='enterDepartment'),
]
