from django.contrib import admin

from .models import PersonalData,Projects
# Register your models here.

admin.site.register(PersonalData)
admin.site.register(Projects)