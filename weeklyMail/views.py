from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello from the weeklymail app.")


def editItem(request, item_id):
    return HttpResponse("This would be item #%s" % item_id)