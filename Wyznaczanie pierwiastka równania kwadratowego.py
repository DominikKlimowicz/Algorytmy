import math

# wczytanie wartości a, b, c
a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

# obliczenie delty
delta = b**2 - 4*a*c

# sprawdzenie, ile rozwiązań ma równanie
if delta < 0:
    print("Brak rozwiązań rzeczywistych")
elif delta == 0:
    x = -b / (2*a)
    print("Jedno rozwiązanie: ", x)
else:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(f"Dwa rozwiązania: {x1},{x2}")
