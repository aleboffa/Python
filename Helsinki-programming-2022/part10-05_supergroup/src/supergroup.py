# Write your solution here:
#from typing_extensions import Self


class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup(SuperHero):
    def __init__(self, name: str, location: str):
        self._name = name
        self._members = []
        self._location = location

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    def print_group(self):
        print(f"{self.name}, {self.location}")
        print("Members:")
        for member in self._members:
            print(member)

if __name__ == "__main__":
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()