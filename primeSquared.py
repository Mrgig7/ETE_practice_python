def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def print_squared_primes(n):
    primes = find_primes(n)
    squared_primes = [x**2 for x in primes]
    if squared_primes:
        print(squared_primes)
    else:
        print("No prime numbers found.")

n = int(input("Enter an integer n: "))
print_squared_primes(n)
