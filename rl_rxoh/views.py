from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("코딩 쉽다!!(?) 완전")

def index(request):
    return render(request, "index.html", {"hello": "루오"})