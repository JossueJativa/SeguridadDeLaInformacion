from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.enterAsset, name='enterAsset'),
    path('tableAssets/', views.tableAssets, name='tableAssets'),
    path('deleteTableAssets/<str:id>/', views.deleteTableAssets, name='deleteTableAssets'),
    path('editTableAssets/', views.editTableAssets, name='editTableAssets'),
    path('enterUsers/', views.enterUsers, name='enterUsers'),
    path('tableusers/', views.tableusers, name='tableusers'),
    path('deleteTableUsers/<str:id>', views.deleteTableUsers, name='deleteTableUsers'),
    path('editTableUsers/', views.editTableUsers, name='editTableUsers'),
    path('enterDepartment/', views.enterDepartment, name='enterDepartment'),
    path('tabledepartments/', views.tabledepartments, name='tabledepartments'),
    path('deleteTableDepartments/<str:id>', views.deleteTableDepartments, name='deleteTableDepartments'),
    path('editTableDepartments', views.editTableDepartments, name='editTableDepartments'),
    path('asingRiskAsset/', views.asingRiskAsset, name='asingRiskAsset'),
    path('tableRisks/', views.tableRisks, name='tableRisks'),
    path('deleteTableRisks/<str:id>', views.deleteTableRisks, name='deleteTableRisks'),
    path('editTableRisks/', views.editTableRisks, name='editTableRisks'),
    path('enterSafeguards/', views.enterSafeguards, name='enterSafeguards'),
    path('tableSafeguards/', views.tableSafeguards, name='tableSafeguards'),
    path('deleteTableSafeguards/<str:id>', views.deleteTableSafeguards, name='deleteTableSafeguards'),
    path('editTableSafeguards/', views.editTableSafeguards, name='editTableSafeguards'),
    path('get-subtypes/<int:type_id>/', views.get_subtypes, name='get_subtypes'),
    path('get-workloads/', views.get_workloads, name='get_workloads'),
    path('get-departments/', views.get_departments, name='get_departments'),
    path('get-dependentAssets/', views.get_dependentAssets, name='get_dependentAssets'),
    path('get-assets/', views.get_assets, name='get_assets'),
    path('get-types/', views.get_types, name='get_types'),
    path('get-subtypes2/', views.get_subtypes2, name='get_subtypes2'),
    path('get-users/', views.get_users, name='get_users'),
    path('get-risks/<int:risktype_id>', views.get_risks, name='get_risks'),
    path('get-risktypes/', views.get_risktypes, name='get_risktypes'),
    path('get-safeguardstypes/', views.get_safeguardstypes, name='get_safeguardstypes'),
    path('get-safeguards/<int:safeguardstype_id>/', views.get_safeguards, name='get_safeguards'),

    path('profile/', views.userProfile, name='userProfile'),
]