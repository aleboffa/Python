# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie={}
    movie={"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(movie)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)


# person1 = {"name": "Pippa Python", "height": 154, "weight": 61, "age": 44}
# person2 = {"name": "Peter Pythons", "height": 174, "weight": 103, "age": 31}
# person3 = {"name": "Pedro Python", "height": 191, "weight": 71, "age": 14}
# people = [person1, person2, person3]