from django.db import models

class ToDoItem(models.Model):
    added_by = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} (Added by: {self.added_by})"
