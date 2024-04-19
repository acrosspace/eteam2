from django.shortcuts import render

from .functions import eratosthenes
from .functions import isPrime

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world!")

def index(request):
    return render(request, "index.html", {"hello": "유원"})

def test(request):
    #n = request.GET.get('n', 100)  # 사용자로부터 받은 n 값, 기본값 100
    #n = int(n)
    primes = eratosthenes(10)
    #primes = isPrime(10)
    return render(request, "test.html", {"primes": primes})

def test2(request, n):
    primes = eratosthenes(n)

    primes = [p * 10 for p in primes]

    return render(request, "test2.html", {"primes": primes})
