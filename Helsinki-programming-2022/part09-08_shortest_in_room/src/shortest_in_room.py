# WRITE YOUR SOLUTION HERE:
from os import name
from queue import Empty

class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.room = []
        self.tot_height = 0

    def add(self, person: Person):
        self.room.append(person)
        self.tot_height += person.height

    def is_empty(self):
        if len(self.room) == 0:
            return True
        return False

    def print_contents(self):
        print(f"There are {len(self.room)} persons in the room, and their combined height is {self.tot_height} cm")
        for people in self.room:
            print(f"{people.name} ({people.height} cm)")

    def shortest(self):
        shortest_one = 1000
        if len(self.room) == 0:
            return None
        else:
            for people in self.room:
                if shortest_one > people.height: 
                    short_one = people
                    shortest_one = people.height
        return short_one

    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person == None:
            return None
        else:
            self.room.remove(shortest_person)
        return shortest_person



if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()

# There are 4 persons in the room, and their combined height is 683 cm
# Lea (183 cm)
# Kenya (172 cm)
# Nina (162 cm)
# Ally (166 cm)

# Removed from room: Nina

# There are 3 persons in the room, and their combined height is 521 cm
# Lea (183 cm)
# Kenya (172 cm)
# Ally (166 cm)

