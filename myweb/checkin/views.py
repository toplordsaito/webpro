from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dailyTable(req, teacherId):
    return HttpResponse("Daily Table Page %s" %teacherId)

def course(req, courseId):
    return HttpResponse("Course %s" %courseId)

def checkin(req, qrCode):
    return HttpResponse("QrCode Scan Here %s" %qrCode)