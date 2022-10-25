# Write your solution here
import json
from unicodedata import name

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

    students = json.loads(data)
    for student in students:
        nombre=student["name"]
        edad=student["age"]
        hobbies=", ".join(student["hobbies"])

        print(f"{nombre} {edad} years ({hobbies})" )

#   Peter Pythons 27 years (coding, knitting)
#   Jean Javanese 24 years (coding, rock climbing, reading)

if __name__ == "__main__":

    print_persons("file1.json")

#    print(', '.join(lst))