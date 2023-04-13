wektor = [4, 8, 2, 10, 5, 7, 1, 3, 9, 6]
n = len(wektor)

if n == 1:
    najwiekszy = wektor[0]
else:
    srodek_indeks = n // 2
    najwiekszy_lewej = wektor[0]
    i = 1
    while i < srodek_indeks:
        if wektor[i] > najwiekszy_lewej:
            najwiekszy_lewej = wektor[i]
        i += 1
    najwiekszy_prawej = wektor[srodek_indeks]
    i = srodek_indeks + 1
    while i < n:
        if wektor[i] > najwiekszy_prawej:
            najwiekszy_prawej = wektor[i]
        i += 1
    najwiekszy = najwiekszy_lewej if najwiekszy_lewej > najwiekszy_prawej else najwiekszy_prawej

print(najwiekszy)
