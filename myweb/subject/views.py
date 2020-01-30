from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def views(req):
    return HttpResponse("views Subject Page")

def add(req):
    return HttpResponse("add Subject Page")

def edit(req):
    return HttpResponse("edit Subject Page")
