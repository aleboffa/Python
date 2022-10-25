# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        frutas={}
        for fruits in new_file:
            fruits = fruits.replace("\n", "")
            parts = fruits.split(";")
            name = parts[0]
            price = parts[1]
            frutas[name]=float(price)
    return frutas
