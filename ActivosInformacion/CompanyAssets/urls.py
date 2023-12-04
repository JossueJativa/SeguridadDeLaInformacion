from django.urls import path
from . import views

app_name = "Assets"

urlpatterns = [
    path("", views.companyassets, name="companyassets"),
    path("editCompanyAssets/", views.editCompanyAssets, name="editCompanyAssets"),
    path("deleteCompanyAssets/<int:id>", views.deleteCompanyAssets, name="deleteCompanyAssets"),
    path("origin/", views.origin, name="origin"),
    path("editOrigin/", views.editOrigin, name="editOrigin"),
    path("deleteOrigin/<int:id>", views.deleteOrigin, name="deleteOrigin"),
]
