n = int(input("Podaj długość ciągu: "))

i = 1
ujemne = 0

while i <= n:
    x = int(input(f"Podaj {i} liczbę całkowitą: "))
    if x < 0:
        ujemne += 1
    i += 1

print("Ilość liczb ujemnych w ciągu:", ujemne)
