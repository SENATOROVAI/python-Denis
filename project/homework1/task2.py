
def print_sum(n):
    suma = 0
    while n > 0:
        digit = n % 10
        suma += digit
        n //= 10
    return suma


print_sum(1234567890)  # prints 45
