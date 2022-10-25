# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observs = []
        self.__latest = ""


    def add_observation(self, observation: str):
        self.__observs.append(observation)
        self.__latest = observation


    def latest_observation(self):
        return self.__latest


    def number_of_observations(self):
        return len(self.__observs)


    def __str__(self):
        return f"{self.__name}, {len(self.__observs)} observations"


    # @property
    # def owner(self):
    #     return self.__owner

    # @owner.setter
    # def owner(self, owner):
    #     if owner != "":
    #         self.__owner = owner
    #     else:
    #         raise ValueError("The owner may not be an empty string")





if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)

