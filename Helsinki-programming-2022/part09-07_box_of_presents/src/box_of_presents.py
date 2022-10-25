# WRITE YOUR SOLUTION HERE:
#from turtle import window_height


class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
                
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.present = []
        self.tot_weight = 0

    def add_present(self, present: Present):
        self.present.append(present)
        self.tot_weight += present.weight

    def total_weight(self):

        return self.tot_weight


if __name__ == "__main__":
    book = Present("ABC Book", 2)
    print(book.name)
    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())

# The name of the present: ABC Book
# The weight of the present: 2
# Present: ABC Book (2 kg)