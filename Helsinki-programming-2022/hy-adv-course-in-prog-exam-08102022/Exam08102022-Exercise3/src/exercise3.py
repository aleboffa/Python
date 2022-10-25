from random import shuffle

def draw(my_list):
    elements = []
    num = 0
    for item in my_list:
        elements.append(item)
    elements = list(set(elements))
    shuffle(elements)
    if elements == []:
        raise Exception("Sorry, no animals in the list")
    for i in range(len(elements)):
        num += 1
        if num > len(elements):
            raise Exception("Sorry, no more animals") 
        else:
            yield elements[i]



###########################
if __name__=="__main__":
    animal_generator = draw(['Chicken', 'Bear', 'Gorilla', 'Fox'])
    for i in range(4):
        print(next(animal_generator))

# Sample output:

# Bear
# Fox
# Chicken
# Gorilla

# raise Exception("Sorry, no numbers below zero")