# Write your solution here
import json
from optparse import Values
from os import name

# file is in .json format
file =  input("file name: ") #"partial.json" #

with open(file) as my_file:
    data = my_file.read()

partials = json.loads(data)
# for partial in partials:
#     print(partial)

print(f"read the data of {len(partials)} players")
print()

print("commands: ")
print("0 quit")
print("1 search for player")
print("2 teams")
print("3 countries")
print("4 players in team")
print("5 players from country")
print("6 most points")
print("7 most goals")
while True:
    print()
    opt = int(input("command: "))

    if opt == 0: # quit
        break

    elif opt == 1: #   1 search for player
        player = input("name: ")
#        linea =[]
        for partial in partials:
            if partial["name"] == player:
                nombre = partial["name"]
                equipo = partial["team"]
                asist = partial["assists"]
                goles = partial["goals"]

#                print("partial ",partial)
                print(f"{nombre:21}{equipo:3} {goles:3} + {asist:2} = {(asist+goles):3}")
                break

    elif opt == 2: # 2 teams
        equipos = []
        for partial in partials:
            if partial["team"] not in equipos:
                equipos.append(partial["team"])

        equipos=sorted(equipos)
        for equipo in equipos:
            print(equipo)

    elif opt == 3: # 3 countries
        paises = []
        for partial in partials:
            if partial["nationality"] not in paises:
                paises.append(partial["nationality"])

        paises=sorted(paises)
        for pais in paises:
            print(pais) 

    elif opt == 4: # 4 players in team
        equipo_elegido = input("team: ") # "WSH" #
        print()
        jugadores = []

        for partial in partials:
            if equipo_elegido == partial["team"]:
                jugadores.append(partial)
# ORDENAR LA LISTA DE DICCIONARIOS POR VALORES EN PYTHON - USANDO LA FUNCIÓN LAMBDA
#  ######### Por Name ###########
# "jugadores" es una lista de diccionarios
        jugadores=sorted(jugadores, key = lambda i: i["name"])
        # print(jugadores)

        for jugador in jugadores:
            nombre = jugador["name"]
            equipo = jugador["team"]
            asist = jugador["assists"]
            goles = jugador["goals"]
            print(f"{nombre:21}{equipo:3} {goles:3} + {asist:2} = {(asist+goles):3}")   

    elif opt == 5: # 5 players from country
        pais_elegido = input("country: ")
        print()
        jugadores = []
        for partial in partials:
            if pais_elegido == partial["nationality"]:
                jugadores.append(partial)
# ORDENAR LA LISTA DE DICCIONARIOS POR VALORES EN PYTHON - USANDO LA FUNCIÓN LAMBDA-
# #########  Puntos Totales De Mayor a Menor(Goals+Assists) ############
# "jugadores" es una lista de diccionarios
        jugadores=sorted(jugadores, key = lambda i: i["goals"]+i["assists"], reverse=True)
        for jugador in jugadores:
            nombre = jugador["name"]
            equipo = jugador["team"]
            asist = jugador["assists"]
            goles = jugador["goals"]
            print(f"{nombre:21}{equipo:3} {goles:3} + {asist:2} = {(asist+goles):3}") 

    elif opt == 6: # 6 most points, list of n players who've scored the most points
        cant_jugador = int(input("how many: "))
        print()
        jugadores = []
        for partial in partials:
            jugadores.append(partial)
# ORDENAR LA LISTA DE DICCIONARIOS POR VALORES EN PYTHON - USANDO LA FUNCIÓN LAMBDA-
# #########  Por Cant de jugadores con mayor puntos Totales De Mayor a Menor(Goals+Assists) ############
# "jugadores" es una lista de diccionarios
        jugadores=sorted(jugadores, key = lambda i: i["goals"]+i["assists"], reverse=True)
        x=1
        for jugador in jugadores:
            if x > cant_jugador:
                break
            nombre = jugador["name"]
            equipo = jugador["team"]
            asist = jugador["assists"]
            goles = jugador["goals"]
            print(f"{nombre:21}{equipo:3} {goles:3} + {asist:2} = {(asist+goles):3}") 
            x += 1

    elif opt == 7: # 7 most goals, list of n players who've scored the most goals
        cant_jugador = int(input("how many: "))
        print()
        jugadores = []
        for partial in partials:
            jugadores.append(partial)
# ORDENAR LA LISTA DE DICCIONARIOS POR VALORES EN PYTHON - USANDO LA FUNCIÓN LAMBDA-
# #########  Por Cant de jugadores con mayor puntos Totales De Mayor a Menor(Goals+Assists) ############
# "jugadores" es una lista de diccionarios
        jugadores=sorted(jugadores, key = lambda i: i["games"])
        jugadores=sorted(jugadores, key = lambda i: i["goals"], reverse=True)
#        jugadores=sorted(jugadores, key = lambda i: i["games"])
        x = 1
        for jugador in jugadores:
            if x > cant_jugador:
                break
            nombre = jugador["name"]
            equipo = jugador["team"]
            asist = jugador["assists"]
            goles = jugador["goals"]
            print(f"{nombre:21}{equipo:3} {goles:3} + {asist:2} = {(asist+goles):3}")
            x += 1

######### 2 primeros registros contenido partial.json #########
# {
#     "name": "Patrik Laine","nationality": "FIN","assists": 35,"goals": 28,"penalties": 22,"team": "WPG","games": 68
#     "name": "Andy Greene" ,"nationality": "USA","assists": 12,"goals":  2,"penalties": 16,"team": "NYI","games": 63
#    }
#########################################
#########################################
#      SOLUCION DEL PROFESOR
# import json
 
# class Statistics:
#     def __init__(self, players: list):
#         self.__players = players
 
#     def by_points(self,  p):
#         return  p['goals'] + p['assists']
 
#     def by_goals(self,  p):
#         # if the numbe of goals is equal, less played games is better
#         return (p['goals'], -p['games'])
 
#     def player_data(self, name: str):
#         for player in self.__players:
#             if player['name'] == name:
#                 return player
 
#         return None
 
#     def countries(self):
#         return sorted(list(set(p['nationality'] for p in self.__players )))
 
#     def teams(self):
#         return sorted(list(set(p['team'] for p in self.__players )))
 
#     def players_in_team(self, team: str):
#         players = [ p for p in self.__players if p['team'] == team]
#         return sorted(players, key=self.by_points, reverse=True)
 
#     def players_from_country(self, country: str):
#         players = [ p for p in self.__players if p['nationality'] == country]
#         return sorted(players, key=self.by_points, reverse=True)
 
#     def most_points(self, countryra):
#         players = sorted(self.__players, key=self.by_points, reverse=True)
#         return players[0: countryra]
 
#     def most_goals(self, countryra):
#         players = sorted(self.__players, key=self.by_goals, reverse=True)
#         return players[0: countryra]
 
# class Application:
#     def __init__(self):
#         self.__statistics = None
 
#     def instructions(self):
#         instructions = """
# commands:
# 0 quit
# 1 search for player
# 2 teams
# 3 countries
# 4 players in team
# 5 players from country
# 6 most points
# 7 most goals"""
#         print(instructions)
 
#     def f(self, p: dict):
#         """
#             helper method, which creates a string out of players formatted for output
#         """
#         points = p['goals'] + p['assists']
#         return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"
 
#     def read_file(self):
#         file_name = input("file: ")
#         with open(file_name) as file:
#             data = file.read()
 
#         players = json.loads(data)
#         print(f"read the data of {len(players)} players")
#         self.__statistics = Statistics(players)
 
#     def get_playes(self):
#         name = input("name: ")
#         player = self.__statistics.player_data(name)
#         if player:
#             print(self.f(player))
 
#     def get_teams(self):
#         for team in self.__statistics.teams():
#             print(team)
 
#     def get_countries(self):
#         for country in self.__statistics.countries():
#             print(country)
 
#     def players_in_team(self):
#         team = input("team: ")
#         for player in self.__statistics.players_in_team(team):
#             print(self.f(player)) 
 
#     def players_from_country(self):
#         country = input("country: ")
#         for player in self.__statistics.players_from_country(country):
#             print(self.f(player)) 
 
#     def most_points(self):
#         number = int(input("how many: "))
#         for player in self.__statistics.most_points(number):
#             print(self.f(player)) 
 
#     def most_goals(self):
#         number = int(input("how many: "))
#         for player in self.__statistics.most_goals(number):
#             print(self.f(player)) 
 
#     def execute(self):
#         self.read_file()
#         self.instructions()
#         while True:
#             print()
#             command = input("command: ")
#             if command == "0":
#                 return
#             elif command == "1":
#                 self.get_playes()
#             elif command == "2":
#                 self.get_teams()
#             elif command == "3":
#                 self.get_countries()
#             elif command == "4":
#                 self.players_in_team()
#             elif command == "5":
#                 self.players_from_country()
#             elif command == "6":
#                 self.most_points()
#             elif command == "7":
#                 self.most_goals()
 
# Application().execute()
# # Write your solution here