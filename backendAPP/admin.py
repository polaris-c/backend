from django.contrib import admin
from .models import person

class personAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'composite_info',)

class personAdminComposite(admin.ModelAdmin):
    list_display = ('composite_info',)

admin.site.register(person, personAdminComposite)

print("****** admin is running ******")