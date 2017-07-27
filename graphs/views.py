from django.shortcuts import render
from django.http import HttpResponse

### Note: I have added some stuff in an attempt to get Matplotlib going.
# In reality I should turn here:
# http://scipy-cookbook.readthedocs.io/items/Matplotlib_Django.html
# But for now I'll kludge in a separate file. It never worked here.


def index(request):
    return simple(request)
def simple(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig = Figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=7)
    for i in range(10):
        x.append(now)
        now += delta
        y.append(random.randint(500, 600))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

