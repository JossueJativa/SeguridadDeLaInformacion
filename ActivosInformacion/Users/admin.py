from django.contrib import admin

from Users.models import User, Workload

# Register your models here.
admin.site.register(User)
admin.site.register(Workload)