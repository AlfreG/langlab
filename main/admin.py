
from django.contrib import admin
from .models import Locations, Languages, Menus, Disclaimers

# Register your models here.
admin.site.register(Locations)
admin.site.register(Languages)
admin.site.register(Menus)
admin.site.register(Disclaimers)
