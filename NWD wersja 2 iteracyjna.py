def NWD(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
print(NWD(12,18))
print(NWD(28,24))