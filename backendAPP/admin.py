from django.contrib import admin
from .models import person

class personAdmin(admin.ModelAdmin):
	list_display = ('name', 'age',)
print("****** admin! ******")
admin.site.register(person)
