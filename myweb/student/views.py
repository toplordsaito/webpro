from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def views(req):
    return HttpResponse("views student Page")

def add(req):
    return HttpResponse("add Student Page")

def edit(req):
    return HttpResponse("edit Student Page")
