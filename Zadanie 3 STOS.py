from Stos1 import Stack

def symbolChecker(symbolString):
    stack = Stack()
    otwarte_symbole = "([{"
    zamkniete_symbole = ")]}"
    for symbol in symbolString:
        if symbol in otwarte_symbole:
            stack.push(symbol)
        elif symbol in zamkniete_symbole:
            if stack.isEmpty():
                return False
            poprzedni_symbol = stack.pop()
            if not zgodnosc(poprzedni_symbol, symbol):
                return False
    return stack.isEmpty()

def zgodnosc(otwarty, zamkniety):
    if otwarty == "(" and zamkniety == ")":
        return True
    if otwarty == "[" and zamkniety == "]":
        return True
    if otwarty == "{" and zamkniety == "}":
        return True
    return False
print(symbolChecker('[{{{()}}}]'))
print(symbolChecker('[{{{()[][][]]]][[[[[[[]]]}}}]'))