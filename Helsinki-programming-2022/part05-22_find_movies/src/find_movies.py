# Write your solution here
from unicodedata import name


def find_movies(database: list, search_term: str):

    new_database=[]
    nombre =""
    for movie in database:
        nombre =  movie["name"]
        if search_term.upper() in nombre.upper():
            new_database.append(movie)
    return new_database





if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)