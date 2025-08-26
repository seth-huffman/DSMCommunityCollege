#######################################
# NEW CODE ADDED - START
#######################################
import os
from django.shortcuts import render, redirect
from .models import Task
import numpy
import pandas
from django.conf import settings
from datetime import date

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot

def home(request):

    # Task Two: Some level of user interaction
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        Task.objects.create(title = title, due_date = due_date)
        return redirect('home')

    # Task One: A read/write functionality of some sort with substance.
    tasks = Task.objects.all()

    # Task Three: NumPy
    # Gets the min/max/mean of the due dates
    due = numpy.array([(task.due_date - date.today()).days for task in tasks])
    mean = numpy.mean(due)

    if due.size > 0:
        min = numpy.min(due)
    else:
        min = None

    if due.size > 0:
        max = numpy.max(due)
    else:
        max = None

    # Task Four: Pandas with some kind of transformation (more than reading the frame)
    data = {
        'Title': [task.title for task in tasks],
        'Due Date': [task.due_date for task in tasks],
        'Days Left': [(task.due_date - date.today()).days for task in tasks]
    }

    dataframe = pandas.DataFrame(data)

    # Task Five and Six: Django site & Visualization
    direct = os.path.join(settings.BASE_DIR, 'main', 'static')
    if not os.path.exists(direct):
        os.makedirs(direct)
    path = os.path.join(direct, 'chart.png')

    matplotlib.pyplot.bar(dataframe['Title'], dataframe['Days Left'], color = 'skyblue')
    matplotlib.pyplot.title('Days Until Task Due')
    matplotlib.pyplot.xticks(rotation = 90, ha = 'right')
    matplotlib.pyplot.savefig(path)
    matplotlib.pyplot.close()

    context = {
        'tasks': tasks,
        'mean': mean,
        'min': min,
        'max': max,
        'dataframe_html': dataframe.to_html(index=True),
        'chart_url': 'main/static/chart.png',
    }

    return render(request, 'main/index.html', context)

#######################################
# NEW CODE ADDED - END
#######################################