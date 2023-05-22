from Kolejka import Queue
import random

kolejka=Queue()
kolejka.enqueue('Jacek')
kolejka.enqueue('Janusz')
kolejka.enqueue('Grażyna')
kolejka.enqueue('Piotr')
kolejka.enqueue('Rafał')


while kolejka.size() != 1:
    x=random.randint(1, 20)
    while x > 0:
        kolejka.enqueue(kolejka.denqueue())
        x-=1
    print(kolejka.denqueue())
print("To co zostało w kolejce")
print(kolejka.size())
print(kolejka.denqueue())