def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(97))
