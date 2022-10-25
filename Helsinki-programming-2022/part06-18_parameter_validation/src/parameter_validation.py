# Write your solution here
def new_person(name: str, age: int):
    tupla = (name,age)
    if name == "" or name.count(" ")<1 or len(name)>40 or age<0 or age>150:
        raise ValueError ("There are errors")
    print("todo ok")
    return tupla
     
    
    

############################
###############################################
if __name__=="__main__":
    number = new_person('Andrew', 32)

# name is an empty string
# name contains less than two words
# name is longer than 40 characters
# age is a negative number
# age is greater than 150

######################################
##
## solucion profesor
##
##################################
# def new_person(name: str, age: int):
#     # Validate name
#     if name == "" or (" " not in name) or len(name) > 40:
#         raise ValueError("Invalid argument value for name: " + name)
 
#     # Validate age
#     if age < 0 or age > 150:
#         raise ValueError("Invalid argument value for age:" + str(age))
 
#     # Both ok
#     return (name, age)