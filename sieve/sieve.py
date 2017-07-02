def sieve(n: int) -> list:
    """
    Sieve away and only primes are left.
    """
    primes = 2*[False] + (n-1)*[True]
    for i in range(2, int(n**0.5+1.5)):
        for j in range(i*i, n+1, i):
            primes[j] = False
    return [prime for prime, checked in enumerate(primes) if checked]


if __name__ == '__main__':
    print(sieve(100))
