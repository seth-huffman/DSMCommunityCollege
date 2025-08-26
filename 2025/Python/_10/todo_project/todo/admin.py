from django.contrib import admin
from .models import ToDoItem

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'added_by', 'added_on', 'due_date', 'is_completed')
    list_filter = ('is_completed', 'due_date', 'added_by')
    search_fields = ('description', 'added_by')