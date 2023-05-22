from Stos1 import Stack

def oblicz(x, y, a):
    if a == '+':
        return x+y
    elif a == '-':
        return x-y
    elif a == '/':
        return x/y
    elif a == '*':
        return x*y
    elif a == '^':
        return x**y

s=Stack()
a=0
while a != '=':
    a=input('Podaj liczbę lub znak działania')
    if a == '=':
        break
    if a in ['+' , '-' , '/' , '*' ,'^']:
        operator2=s.pop()
        operator1=s.pop()
        wynik=oblicz(operator1, operator2, a)
        s.push(wynik)
    else :
        a=int(a)
        s.push(a)
print(s.pop())