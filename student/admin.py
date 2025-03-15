from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'course']
    search_fields = ['name', 'email', 'phone', 'course']
    list_filter = ['course']

admin.site.register(Student,StudentAdmin)
