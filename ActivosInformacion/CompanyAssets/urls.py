from django.urls import path
from . import views

app_name = "Assets"

urlpatterns = [
    path("", views.companyassets, name="companyassets"),
    path("origin/", views.origin, name="origin"),
    path("editOrigin/", views.editOrigin, name="editOrigin"),
    path("deleteOrigin/<int:id>", views.deleteOrigin, name="deleteOrigin"),
]
