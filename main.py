import math

def pythagorean_theorem(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# Пример использования
a = 3
b = 4
c = pythagorean_theorem(a, b)
print(f"Для a = {a} и b = {b}, гипотенуза c = {c}")
