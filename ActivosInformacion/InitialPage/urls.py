from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.enterAsset, name='enterAsset'),
    path('enterUsers/', views.enterUsers, name='enterUsers'),
    path('tableusers/', views.tableusers, name='tableusers'),
    path('deleteTableUsers/<str:id>', views.deleteTableUsers, name='deleteTableUsers'),
    path('enterDepartment/', views.enterDepartment, name='enterDepartment'),
    path('tabledepartments/', views.tabledepartments, name='tabledepartments'),
    path('deleteTableDepartments/<str:id>', views.deleteTableDepartments, name='deleteTableDepartments'),
]
