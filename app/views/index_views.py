from django.shortcuts import render
from django.http import HttpResponse
from django.template import context


def index(request):
    return render(request, "./index.html")