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
