def search_by_name(file,word):
    recipes = []
    with open(file) as new_file:
        for line in new_file:
            recipes.append(line.strip())

    lista=[]
    for tx in recipes:
        if word in tx.lower():
            if tx[0].isupper():
                lista.append(tx)
    return lista

def search_by_time(filename: str, prep_time: int):
    recipes = []
    with open(filename) as new_file:
        for line in new_file:
            recipes.append(line.strip())  
    lista=[]
    for tx in recipes:       
        if tx != "":
#            print(tx[0]) 
            if tx[0].isupper():
                titulo = tx + ", "  
            else:
#                print(type(tx))
                if tx[0] in "0123456789":
                    if int(tx) <= prep_time:
                        line = titulo + "preparation time " + str(tx) + " min" #### Pancakes, preparation time 15 min
                        lista.append(line)
#                       print("linea: ",line)
        else:
            continue

    return lista

def search_by_ingredient(filename: str, ingredient: str):
    recipes = []
    with open(filename) as new_file:
        for line in new_file:
            recipes.append(line.strip())  
    lista=[]
    for tx in recipes:       
        if tx != "":
#            print(tx[0]) 
            if tx[0].isupper():
                titulo = tx + ", "  
            else:
#                print(type(tx))
                if tx[0] in "0123456789":
                    time = tx
                if tx == ingredient:
                    line = titulo + "preparation time " + str(time) + " min" #### Pancakes, preparation time 15 min
                    lista.append(line)
#                       print("linea: ",line)
        else:
            continue
    return lista

######################################################
if __name__=="__main__":

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)

##########################################
##  solucion profesor
##
###################################
# def read_file(filename):
#     with open(filename) as file:
#         rows = []
#         for row in file:
#             rows.append(row.strip())
 
#     recipes = []
#     name_in_row = True
#     prep_time_in_row = True
#     new = { "ingredients": []}
#     for row in rows:
#         if name_in_row:
#             new["name"] = row
#             name_in_row = False
#             prep_time_in_row = True
#         elif prep_time_in_row:
#             new["prep_time"] = int(row)
#             prep_time_in_row = False
#         elif len(row) > 0:
#             new["ingredients"].append(row)
#         else:
#             recipes.append(new)
#             name_in_row = True
#             new = {"ingredients": []}
#     recipes.append(new)
 
#     return recipes
 
# def search_by_name(filename: str, word: str):
#     recipes = read_file(filename)
 
#     found = []
#     for recipe in recipes:
#         if word.lower() in recipe["name"].lower():
#             found.append(recipe["name"])
 
#     return found
 
# def search_by_time(filename: str, time: int):
#     recipes = read_file(filename)
 
#     found = []
#     for recipe in recipes:
#         if recipe["prep_time"] <= time:
#             found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
#     return found
 
# def search_by_ingredient(filename: str, ingredient: str):
#     recipes = read_file(filename)
 
#     found = []
#     for recipe in recipes:
#         if ingredient.lower() in recipe["ingredients"]:
#             found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
#     return found
# # Write your solution here