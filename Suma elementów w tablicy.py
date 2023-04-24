Tablica = [1, 2, 3, 4, 5, 6]
n = len(Tablica)
wynik = 0
c=0
zmieniona = Tablica
TZ=0

while c <= len(Tablica):
    n=len(Tablica)-c
    zmieniona = Tablica[TZ:]
    while n > 0:
        if n == 1:
            wynik += zmieniona[0]
            break
        mid = n // 2
        n = mid
        zmieniona = zmieniona[:mid]
    c+=1
    TZ+=1
print(wynik)
