# Write your solution here:

class Item:
    def __init__(self, name: str, weight: int):
        # calling the setter method for the name attribute
        self.__name = name
        self.__weight = weight
  
    def name(self):
        return self.__name
  
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
##############################
class Suitcase:
    def __init__(self, max_weight: int):
        self.item = []
        self.max_weight = max_weight
        self.tot_weight = 0
        self.cant_items = 0

    def add_item(self, item: Item):
        if (self.tot_weight + item.weight()) <= self.max_weight:
            self.tot_weight += item.weight()
            self.item.append(item)
            self.cant_items += 1

    @property
    def name(self):
        return self.name


    def print_items(self):
        for thing in self.item:
            print(f"{thing.name()} ({thing.weight()} kg)")

    def weight(self):
        return self.tot_weight

    def heaviest_item(self):
        heaviest_one = 0
        if len(self.item) == 0:
            return None
        else:
            for thing in self.item:
                if heaviest_one < thing.weight(): 
                    heavy_one = thing
                    heaviest_one = thing.weight()
        return heavy_one


    def __str__(self):
        if self.cant_items != 1:
            return f"{self.cant_items} items ({self.tot_weight} kg)"
        else:
            return f"{self.cant_items} item ({self.tot_weight} kg)"    
##############################
class CargoHold(Suitcase):
    def __init__(self, max_weig: int):
        self.cargo = []
        self.max_weig = max_weig
        self.tot_cargo_weig = 0
        self.cant_suitcases = 0

    def add_suitcase(self, suit: Suitcase):
        if (self.tot_cargo_weig + suit.weight()) <= self.max_weig:
            self.tot_cargo_weig += suit.weight()
            self.cargo.append(suit)
            self.cant_suitcases += 1
            
    def print_items(self):
        for thing in self.item:
#            print(thing.weight())
            print(f"{cargo.name()} ({thing.weight()} kg)")
#            print(f"({thing.weight()} kg)")

    # def print_items(self):
    #     for suitcase in self.cargo:
    #         for item in suitcase:
    #             print(f"({item.weight()} kg)")

    def __str__(self):
        if self.cant_suitcases != 1:
            return f"{self.cant_suitcases} suitcases, space for {self.max_weig - self.tot_cargo_weig} kg" 
        else:
            return f"{self.cant_suitcases} suitcase, space for {self.max_weig - self.tot_cargo_weig} kg"    

#######################################
if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()