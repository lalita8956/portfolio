from django.shortcuts import render , HttpResponse
import requests


def index(request):
    return render(request,template_name="website/index.html")

def assets(request):
    return render(request,template_name="website/assets")

    
