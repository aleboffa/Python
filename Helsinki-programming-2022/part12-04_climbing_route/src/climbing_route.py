class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# orden por longitud
def order_by_len(item: tuple):
    return item.length

def sort_by_length(routes: list):
    return sorted(routes, key=order_by_len, reverse=True)

# order by difficulty
def order_by_grade(item: tuple):
    return item.grade

def sort_by_difficulty(routes: list):
#   return ordenado primero por longitud y despues por grado dificult
    return sorted((sorted(routes, key=order_by_len, reverse=True)), key=order_by_grade, reverse=True)

#############################################
if __name__ == "__main__":

    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]
    for route in sort_by_difficulty(routes):
        print(route)

# Edge, length 38 metres, grade 6A+
# Synchro, length 14 metres, grade 8C+
# Small steps, length 12 metres, grade 6A+
# Smooth operator, length 9 metres, grade 7A
################################################
##### profesor solution
#####
# class ClimbingRoute:
#     def __init__(self, name: str, length: int, grade: str):
#         self.name = name
#         self.length = length
#         self.grade = grade
 
#     def __str__(self):
#         return f"{self.name}, length {self.length} metres, grade {self.grade}"
 
# def sort_by_length(routes: list):
#     def length_order(route):
#         return route.length
 
#     return sorted(routes, key=length_order, reverse=True)
 
# def sort_by_difficulty(routes: list):
#     def difficulty_order(route):
#         return (route.grade, route.length)
 
#     return sorted(routes, key=difficulty_order, reverse=True)