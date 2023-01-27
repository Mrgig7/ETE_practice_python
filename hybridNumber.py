def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_hybrid(n):
    if n < 1:
        return None
    lower = int('1' + '0' * (n-1))
    upper = int('9' * n)
    for i in range(upper, lower-1, -1):
        if is_prime(i):
            if str(i) == str(i)[::-1]:
                return i
    return None

print(generate_hybrid(1))