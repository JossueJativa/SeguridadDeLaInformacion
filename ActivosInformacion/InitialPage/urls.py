from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
    path('typesActives/', views.typesActives, name='typesActives'),
    path('subtypesActives/', views.subtypesActives, name='subtypesActives'),
]
