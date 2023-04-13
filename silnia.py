def silnia(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik
print(silnia(int(input())))