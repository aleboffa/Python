import random

def roll(die: str):
#    num = 0
    die_a =[3, 3, 3, 3, 3, 6]
    die_b =[2, 2, 2, 5, 5, 5]
    die_c =[1, 4, 4, 4, 4, 4]
    if die == "A":
        num = random.choice(die_a)
    elif die == "B":
        num = random.choice(die_b)
    elif die == "C":
        num = random.choice(die_c)
#    print(type(num))
    return num

def play(die1: str, die2: str, times: int):
#    tupla = ()
    cont_die1 = 0
    cont_die2 = 0
    cont_tie = 0
#    num1, num2 = []
    for x in range(1,times+1):
        num1=roll(die1)
        num2=roll(die2)
        if num1 > num2:
            cont_die1 += 1
        elif num1 < num2:
            cont_die2 += 1
        else: 
            cont_tie +=1  

    return (cont_die1,cont_die2,cont_tie)


####################################
if __name__=="__main__":
    result = play("A", "C", 10)
    print(result)
    result = play("B", "B", 10)
    print(result)

###################################
####
####   solucion profesor
####
###################################
# from random import sample
# def roll(die: str):
#     dices = {
#         "A": [3, 3, 3, 3, 3, 6],
#         "B": [2, 2, 2, 5, 5, 5],
#         "C": [1, 4, 4, 4, 4, 4]
#     }
 
#     return sample(dices[die], 1)[0]
 
# def play(die1: str, die2: str, times: int):
#     v1 = 0
#     v2 = 0
#     t = 0
#     for i in range(times):
#         n1 = roll(die1)
#         n2 = roll(die2)
#         if n1>n2:
#             v1 += 1
#         elif n1<n2:
#             v2 += 1
#         else:
#             t += 1
#     return v1, v2, t
 