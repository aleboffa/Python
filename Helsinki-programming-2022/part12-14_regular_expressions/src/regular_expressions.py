# Write your solution here
import re

def is_dotw(my_string: str):
    expression = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"

    while True:
        input_string = my_string
        if input_string == "":
            break
        if re.search(expression, input_string):
            return True
        else:
            return False

def all_vowels(my_string: str):
    expression = "(?=.*[Aa])(?=.*[Ee])(?=.*[Ii])(?=.*[Oo])(?=.*[Uu]).*"
    long =1
    for char in my_string:
        if char not in "aeiou":
            return False
        else:
            if long >= len(my_string):
                return True
            long +=1

def time_of_day(my_string: str):
    expression = "HH:MM:SS"  #[0-23][0-59][0-59]
    hours = my_string[0:2]
    min = my_string[3:5]
    sec = my_string[6:]
    for char in my_string:
        if char.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False

    if int(hours) not in range(0,24):
        return False
    if int(min) not in range(0,60):
        return False
    if int(sec) not in range(0,60):
        return False
    return True

###### Solucion del profesor ###############
############################################
# import re
####################################
# 1- Using a regular expression, please write a function named is_dotw(my_string: str).
#  The function should return True if the string passed as an argument contains an
#   abbreviation for a day of the week (Mon, Tue, Wed, Thu, Fri, Sat, Sun)

# def is_dotw(my_string: str):
#     return re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) is not None
#################################### 
# 2- Please write a function named all_vowels(my_string: str) which uses a regular expression
#  to check whether all characters in the given string are vowels. 

# def all_vowels(my_string: str):
#     return re.search("^[aeiou]*$", my_string) is not None
####################################
# Please write a function named time_of_day(my_string: str) which uses a regular expression to check
#  whether a string in the format XX:YY:ZZ is a valid time in the 24-hour format, with two digits each
#   for hours, minutes and seconds 

# def time_of_day(my_string: str):
#     return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string) is not None

if __name__ == "__main__":

    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))