# Write your solution here
from random import *
from string import *

def generate_strong_password(n, segundo, tercero):
    especial = list("!?=+-()#")
    number = list("0123456789")
    texto = list(ascii_lowercase)
    final = [] 
    shuffle(final)
    if segundo and not tercero:
        for i in range(n-1):
            final.append(choice(texto))
        final.append(choice(number))

    elif tercero and not segundo:
        for i in range(n-1):
            final.append(choice(texto))
        final.append(choice(especial))

    elif segundo and tercero:
        for i in range(n-2):
            final.append(choice(texto))
        final.append(choice(number))
        final.append(choice(especial))
    else:
        final = texto
    shuffle(final)
    passwo = "".join(final[0:n])

    return passwo

if __name__ == "__main__":

    for i in range(10):
        print(generate_strong_password(6, True, True))