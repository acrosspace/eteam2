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

def test3(request, name=None):

    if name:
        name = f"이름은 {name}입니다."
    else:
        name = "이름이 없습니다."

    return render(request, "test3.html", {"name": name})





def test4(request):
    return render(request, "test4.html")








def test4_type(request, object_type):
    return render(request, "test4.html", {"object_type": object_type})

def test5(request):
    return render(request, "test5.html")

def test6(request):
    return render(request, "test6.html")

def test7(request):
    return render(request, "test7.html")

