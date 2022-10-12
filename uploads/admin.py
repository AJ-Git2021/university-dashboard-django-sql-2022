from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Task

class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Task, TaskAdmin)