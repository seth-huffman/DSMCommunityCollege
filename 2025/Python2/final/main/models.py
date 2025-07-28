from django.db import models

#######################################
# NEW CODE ADDED - START
# Connecting the charts up to real data
#######################################
class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()

    def __str__(self):
        return self.title
#######################################
# NEW CODE ADDED - END
#######################################
