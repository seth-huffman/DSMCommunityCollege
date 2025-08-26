#######################################
# NEW CODE ADDED - START
#######################################

from django.test import TestCase
from datetime import date
from .models import Task

class TaskModelTest(TestCase):

    def test_create_task(self):
        task = Task.objects.create(
            title='Orange',
            due_date=date(2000, 1, 1)
        )

        saved_task = Task.objects.get(id=task.id)

        self.assertEqual(saved_task.title, 'Orange')
        self.assertEqual(saved_task.due_date, date(2000, 1, 1))

#######################################
# NEW CODE ADDED - END
#######################################