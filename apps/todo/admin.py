from django.contrib import admin

from apps.todo.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "priority","category",'time_to_do']
    readonly_fields = ["created"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
