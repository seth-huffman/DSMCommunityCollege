from django.shortcuts import render
from .models import ToDoItem

def todo_list(request):
    items = ToDoItem.objects.all().order_by('-added_on')
    return render(request, 'todo_list.html', {'items': items})