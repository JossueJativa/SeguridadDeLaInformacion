from django.urls import path
from Workers import views

app_name = "workers"

urlpatterns = [
    path("", views.userspage, name="userpage"),
    path("edituser/", views.edituser, name="edituser"),
    path("deleteuser/<int:user_id>", views.deleteuser, name="deleteuser"),
    path("departments/", views.departments, name="departments"),
    path("editdepartment/", views.editdepartment, name="editdepartment"),
    path("deletedepartment/<int:department_id>", views.deletedepartment, name="deletedepartment"),
    path("workpositions/", views.workpositions, name="workpositions"),
    path("editworkposition/", views.editworkposition, name="editworkposition"),
    path("deleteworkposition/<int:workposition_id>", views.deleteworkposition, name="deleteworkposition"),
    path("responsabilities/", views.responsabilities, name="responsabilities"),
    path("editresponsability/", views.editresponsability, name="editresponsability"),
    path("deleteresponsability/<int:responsability_id>", views.deleteresponsability, name="deleteresponsability"),
    path("userresponsabilities/", views.userresponsabilities, name="userresponsabilities"),
    path("edituserresponsability/", views.edituserresponsability, name="edituserresponsability"),
    path("deleteuserresponsability/<int:userresponsability_id>", views.deleteuserresponsability, name="deleteuserresponsability"),
]
