def fact(a):
    if a==1 or a==0:
        return 1
    else:
        return a * fact(a-1)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
def fibonacci(n):
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def get_gcd(A, b):
    while b:
        a, b = b, a%b
        return a