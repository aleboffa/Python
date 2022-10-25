# Write your solution here
from fractions import *

def fractionate(amount: int):
    lista=[]
    for p in range(0,amount):
        lista.append(Fraction(1,amount))
    return lista



if __name__ == "__main__":

    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))