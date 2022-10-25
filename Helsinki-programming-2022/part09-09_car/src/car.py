# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol_tank = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol_tank = 60

    def drive(self, km:int):
        rest_tank = self.__petrol_tank - km
        if rest_tank >= 0:
            self.__odometer += km
            self.__petrol_tank -= km
        else:
            self.__odometer += self.__petrol_tank
            self.__petrol_tank = 0

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol_tank} litres"

if __name__ == "__main__":
    car = Car()
    print(car) #1
    car.fill_up()
    print(car) #2
    car.drive(20)
    print(car) #3
    car.drive(50)
    print(car) #4
    car.drive(10)
    print(car) #5
    car.fill_up()
    car.fill_up()
    print(car) #6
# Sample output
# 1 # Car: odometer reading 0 km, petrol remaining 0 litres
# 2 # Car: odometer reading 0 km, petrol remaining 60 litres
# 3 # Car: odometer reading 20 km, petrol remaining 40 litres
##### now DRIVE 40 km more and car stop- without petrol- rest drive 10km (total 50km)
# 4 # Car: odometer reading 60 km, petrol remaining 0 litres - no petrol no drive
# 5 # Car: odometer reading 60 km, petrol remaining 0 litres - no petrol no drive
##### fill tank twice.....60 + 60 litres but only can charge 60litres
# 6 # Car: odometer reading 60 km, petrol remaining 60 litres