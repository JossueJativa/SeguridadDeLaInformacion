from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
    path('typesActives/', views.typesActives, name='typesActives'),
    path('editsTypesActives/', views.editsTypesActives, name='editsTypesActives'),
    path('deleteTypesActives/<int:id>', views.deleteTypesActives, name='deleteTypesActives'),
    path('subtypesActives/', views.subtypesActives, name='subtypesActives'),
    path('editsSubtypesActives/', views.editsSubtypesActives, name='editsSubtypesActives'),
    path('deleteSubtypesActives/<int:id>', views.deleteSubtypesActives, name='deleteSubtypesActives'),
]
