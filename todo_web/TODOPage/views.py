from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    return HttpResponse("Hello Siva")
