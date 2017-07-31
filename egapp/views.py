from django.shortcuts import render
from django.http import HttpResponse

# http://scipy-cookbook.readthedocs.io/items/Matplotlib_Django.html
# Follow 6 includes are from there.... some seem redundant.
import random
import django
import datetime

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from .models import GraphableFunction, Source
from django.http import Http404
from django.shortcuts import render


class FigureHelper:
    """NYI -- refactor to here, or wherever the correct Django place for helpers is."""
    def __init__(self, figure=None):
        raise     """NYI"""

def index(request):
    return simple(request)

#at one point this was an issue, since resolved:
# https://github.com/matplotlib/matplotlib/issues/6023
def simple(request):
    canvas = FigureCanvas(hybrid())
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def display_figure(list_of_functions, color="purple"):
    import numpy as np
    fig = Figure(figsize=(8,6), dpi=80)
    ax = fig.add_subplot(111)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    Ys = []
    for function in list_of_functions:
        Y = (eval(function))
        ax.plot(X, Y, color=color, linewidth=4.5, linestyle=":")
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


def graph_by_id(request, function_id, color="purple"):
    try:
        function = GraphableFunction.objects.get(pk=function_id)
    except GraphableFunction.DoesNotExist:
        raise Http404("This particular GraphableFunction with this ID does not exist") #% function_id)
    canvas = FigureCanvas(display_figure([function.function_spec], color))
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def detail_color(request, function_id, color):
    try:
        function = GraphableFunction.objects.get(pk=function_id)
    except GraphableFunction.DoesNotExist:
        raise Http404("This particular GraphableFunction with this ID does not exist") #% function_id)
#    return render(request, 'polls/detail.html', {'function': function})
    print ("It's time for the function %s" % function)
    canvas = FigureCanvas(display_figure([function.function_spec]))
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    print ("Soon I will attempt with color %s" % color)
    return response


def graph_arbitrary(request, function_spec  ):
    import logging
    logging.warning("TODO: DRY violation in graph_arbitrary")
    canvas = FigureCanvas(display_figure([function_spec]))
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
