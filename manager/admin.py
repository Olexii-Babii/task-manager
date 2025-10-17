from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import (
    Worker,
    TaskType,
    Task,
    Position
)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "deadline", ]
    list_filter = ["priority", ]
    search_fields = ["name", ]
    
    
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display +  ("position", )
    fieldsets = UserAdmin.fieldsets + ((("Additional info"), {"fields": ("position",)}),)
    # add_fieldsets = (UserAdmin.add_fieldsets +
    #                  ((("Additional info"), {"fields": ("first_name", "last_name", "position",)}),))


admin.site.register(TaskType)
admin.site.register(Position)
