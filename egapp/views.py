from django.shortcuts import render
from django.http import HttpResponse

# http://scipy-cookbook.readthedocs.io/items/Matplotlib_Django.html
# Follow 6 includes are from there.... some seem redundant.
import random
import django
import datetime

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

from .models import GraphableFunction, Source
from django.http import Http404
from django.shortcuts import render



def index(request):
    return simple(request)

#at one point this was an issue, since resolved:
# https://github.com/matplotlib/matplotlib/issues/6023
def simple(request):
    canvas = FigureCanvas(hybrid())
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def display_figure(list_of_functions):
    import numpy as np
    fig = Figure(figsize=(8,6), dpi=80)
    ax = fig.add_subplot(111)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    Ys = []
    for function in list_of_functions:
        Y = (eval(function))
        ax.plot(X, Y, color="orange", linewidth=4.5, linestyle=":")
        Ys.append(Y)

    return fig

def hybrid():
    import numpy as np

    fig = Figure(figsize=(8,6), dpi=80)
    ax = fig.add_subplot(111)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    HALF = np.divide(X, 2)
    recipes = [
        "np.cos(X)",
        "np.sin(X)",
        "np.divide(X, 2)",
    ]
    C, S, HALF = eval(recipes[0]), eval(recipes[1]), eval(recipes[2])
    ax.plot(X, C, color="orange", linewidth=4.5, linestyle=":")
    ax.plot(X, S, color="red", linewidth=7.0, linestyle="-.")
    ax.plot(X, HALF, color="blue", linewidth=3.0, linestyle="--")
    fig.autofmt_xdate()
    return fig


# These are pointless names from the Django tutorial. Delete soon
def detail(request, function_id):
    try:
        function = GraphableFunction.objects.get(pk=function_id)
    except GraphableFunction.DoesNotExist:
        raise Http404("This particular GraphableFunction with this ID does not exist") #% function_id)
#    return render(request, 'polls/detail.html', {'function': function})
    print ("It's time for the function %s" % function)
    canvas = FigureCanvas(display_figure([function.function_spec]))
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

    #return HttpResponse("Soon I will graph the function" % function)



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



#No longer in use. Here for reference only

def random_walk_graph():
    fig = Figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    y2 = []

    current_x = 27
    delta = 3
    for i in range(-10, 10):
        x.append(current_x)
        current_x += delta
        coeff = random.randint(0, 3)
        y.append(100 + i^3 + coeff*i^2)
        y2.append(100 + i^3 + random.randint(0, 3)*i^2)
    ax.plot(x, y, '-.')
    ax.plot(x, y2, ':')
    fig.autofmt_xdate()
    return fig

def fun_sine_graph():
    import numpy as np

    fig = Figure(figsize=(8,6), dpi=80)
    ax = fig.add_subplot(111)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    HALF = np.divide(X, 2)

    ax.plot(X, C, color="orange", linewidth=4.5, linestyle=":")
    ax.plot(X, S, color="red", linewidth=7.0, linestyle="-.")
    ax.plot(X, HALF, color="blue", linewidth=3.0, linestyle="--")

    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    return fig
