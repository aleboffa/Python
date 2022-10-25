# Write your solution here
from random import *
from string import *

def generate_password(n):
    texto = list(ascii_lowercase)
    shuffle(texto)
    passwo = "".join(texto[0:n])
    return passwo

if __name__ == "__main__":

    for i in range(10):
        print(generate_password(8))