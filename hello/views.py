from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Hello

def hello(request):
    return HttpResponse("Hello, world!")

def index(request):
    hellos = Hello.objects.all()
    hello = hellos[0]
    hello0 = Hello.objects.get(id=1)
    #return HttpResponse("Hello, " + hello.name + "!")
    #return render(request, "index.html", {"hello": hello.name})
    return render(request, "index.html", {"hello": hello.name})

def test(request, id):
    return HttpResponse("Hello, world!" + str(id) + "!")