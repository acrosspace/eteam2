def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def eratosthenes(n):
    primes = []
    for i in range(2, n+1):
        if isPrime(i):
            primes.append(i)
    return primes











def prime(n):
    primes = []
    for p in range(2, n + 1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            primes.append(p)
    return primes

def storeNumbers(n):
    numbers = []
    i = 1
    while i <= n:
        numbers.append(i)
        i += 1
    return numbers

def storeNumbers2(n):
    numbers = [x in 1 for x in range(1, n + 1)]
    return numbers
