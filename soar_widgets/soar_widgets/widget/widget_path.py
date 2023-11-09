from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from soar_widgets.widget.widget_data import load_data


def component(request):
    return render(request, "widget_template.html", load_data())