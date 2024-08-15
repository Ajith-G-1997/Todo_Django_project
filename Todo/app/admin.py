from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_date', 'updated_date')

admin.site.register(Task, TaskAdmin)