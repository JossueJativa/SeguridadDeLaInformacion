from django.contrib import admin
from InitialPage.models import TypeAssets, SubtypeAssets, Departments, Assets, AssetsDependence, AssetsValue

# Register your models here.
admin.site.register(TypeAssets)
admin.site.register(SubtypeAssets)
admin.site.register(Departments)
admin.site.register(Assets)
admin.site.register(AssetsDependence)
admin.site.register(AssetsValue)