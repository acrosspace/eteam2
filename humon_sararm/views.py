from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")

def index(request):
    return render(request, "index.html", {"hello": "이수영"})

def test(request):
    return render(request, "test.html", {"result": "성공!"})