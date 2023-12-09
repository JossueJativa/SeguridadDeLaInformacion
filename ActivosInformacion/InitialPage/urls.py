from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.enterAsset, name='enterAsset'),
    path('tableAssets/', views.tableAssets, name='tableAssets'),
    path('deleteTableAssets/<str:id>/', views.deleteTableAssets, name='deleteTableAssets'),
    path('enterUsers/', views.enterUsers, name='enterUsers'),
    path('tableusers/', views.tableusers, name='tableusers'),
    path('deleteTableUsers/<str:id>', views.deleteTableUsers, name='deleteTableUsers'),
    path('editTableUsers/', views.editTableUsers, name='editTableUsers'),
    path('enterDepartment/', views.enterDepartment, name='enterDepartment'),
    path('tabledepartments/', views.tabledepartments, name='tabledepartments'),
    path('deleteTableDepartments/<str:id>', views.deleteTableDepartments, name='deleteTableDepartments'),
    path('editTableDepartments', views.editTableDepartments, name='editTableDepartments'),
    path('get-subtypes/<int:type_id>/', views.get_subtypes, name='get_subtypes'),
    path('get-workloads/', views.get_workloads, name='get_workloads'),
    path('get-departments/', views.get_departments, name='get_departments'),
]
