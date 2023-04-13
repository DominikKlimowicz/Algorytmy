n = int(input("Podaj długość tablicy: "))
x = int(input("Podaj wartość, którą chcesz wyszukać: "))

T = []
i = 0

while i < n:
    y = int(input(f"Podaj {i+1} wartość: "))
    T.append(y)
    i += 1

i = 0
znaleziono = False

while i < n and not znaleziono:
    if T[i] == x:
        znaleziono = True
    i += 1

if znaleziono:
    print(f"Wartość {x} występuje w tablicy.")
else:
    print(f"Wartość {x} nie występuje w tablicy.")
