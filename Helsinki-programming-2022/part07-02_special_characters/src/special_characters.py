# Write your solution here
from pickletools import string1
from string import *

def separate_characters(my_string: str):
    string1=""
    string2=""
    string3=""
    texto = ()
    for str in my_string:
        if str in ascii_letters:
            string1 += str
        elif str in punctuation:
            string2 += str
        else:
            string3 += str
        
    texto = (string1, string2, string3)
    return texto
     



if __name__=="__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])