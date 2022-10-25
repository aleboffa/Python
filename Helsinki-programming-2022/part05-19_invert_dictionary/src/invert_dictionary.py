# Write your solution here
from this import s


def invert(dictionary: dict):
    new_dict={}
    for key, value in dictionary.items():
        new_dict[value]=key
    dictionary.clear()


    for key, value in new_dict.items():
 #       item = new_dict[key]
        dictionary[key]=new_dict[key]
   



if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)

    {"first": 1, "second": 2, "third": 3, "fourth": 4}