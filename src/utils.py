def loadPrimes():
    primes = []
    with open('primes-to-100k.txt', 'r') as f:
        for line in f:
            primes.append(int(line.strip()))
    return primes