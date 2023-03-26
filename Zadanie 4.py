def dzies_na_bin(dzies):
    if dzies == 0 or dzies == 1:
        return str(dzies)
    x = str(dzies % 2)
    pozostaly = dzies // 2
    return dzies_na_bin(pozostaly) + x

# Testowanie algorytmu
dzies = 10
bin = dzies_na_bin(dzies)
print(f"Liczba {dzies} w systemie binarnym to: {bin}")