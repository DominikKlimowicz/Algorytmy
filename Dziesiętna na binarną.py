dzies = int(input("Podaj liczbę dziesiętną: "))
binarna = ""
while dzies > 0:
    reszta = dzies % 2
    binarna = str(reszta) + binarna
    dzies = dzies // 2
if binarna == "":
    binarna = "0"
print("Reprezentacja binarna:", binarna)