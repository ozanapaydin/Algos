    for num in range(2, sys.maxsize):
        if all(num % i != 0 for i in range(2, num)):
            primes.append(num)
            i += 1
            if i == q:
                break
