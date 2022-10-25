# we will need the function sqrt from the math module 
import math

def get_station_data(filename: str):
    stations = {}
    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "Longitude":
                continue
            stations[parts[3]] = (float(parts[0]),float(parts[1]))
    return stations

def distance(stations: dict, station1: str, station2: str):

    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2

    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    dist = -1
    x = 0
    claves=[]
    claves=list(stations.keys())

    while x < len(stations):
        station1=claves[x]
        i = 0
        while i < (len(stations)):
            station2=claves[i]
            temp_dist = distance(stations,station1,station2 )
            if temp_dist > dist:
                dist = temp_dist
                last_station1 = station1
                last_station2 = station2
#            print(i,station1,last_station1,"    ",station2,last_station2,dist)
            i += 1
        x += 1
    return (last_station1,last_station2,dist)
    

if __name__=="__main__":

    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)

# Longitude;Latitude;FID;name;total_slot;operative;id
# 24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
# 24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
# 24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003

###############################################
##
##  solucion profesor
##
##
# import math
 
# def get_station_data(filename:str):
#     stations = {}
#     with open(filename) as file:
#         for row in file:
#             parts = row.split(";")
#             if parts[0] == "Longitude":
#                 continue
#             stations[parts[3]] = (float(parts[0]), float(parts[1]))
 
#     return stations
 
# def distance(stations: dict, station1: str, station2: str):
#     longitude1, latitude1 = stations[station1]
#     longitude2, latitude2 = stations[station2]
 
#     # Note, that this
#     # longitude2, latitude2 = stations[station2]
#     # ...is equivalent to
#     #
#     # coordinates = stations[station2]
#     # longitude2 = coordinates[0]
#     # latitude2 = coordinates[0]
 
#     x_as_km = (longitude1-longitude2) * 55.26
#     y_as_km = (latitude1-latitude2) * 111.2
#     return math.sqrt(x_as_km**2 + y_as_km**2)
 
# def greatest_distance(stations: dict):
#     longest = 0
#     for start_station in stations:
#         for end_station in stations:
#             e = distance(stations, start_station, end_station)
#             if e > longest:
#                 station1 = start_station
#                 station2 = end_station
#                 longest = e
 
#     return station1, station2, longest