"""econgraphs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#   Additional from the Django tutorial
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # These are pointless names from the Django tutorial. Delete soon
    # ex: /polls/5/
    url(r'^(?P<function_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<function_id>[0-9]+)/(?P<color>[a-z]+)$', views.detail_color, name='detail_color'),
    url(r'^arbitrary/(?P<function>.+)$', views.arbitrary, name='arbitrary'),
    # ex: /polls/5/results/
    url(r'^(?P<function_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<function_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
