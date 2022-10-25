# Write your solution here
from ast import Return


def who_won(game_board: list):
    cont_1=0
    cont_2=0
    for row in game_board:
        for square in row:
            if square==1:
                cont_1 += 1
            elif square==2:
                cont_2 += 1
    if cont_1 > cont_2:
        return 1
    elif cont_1 < cont_2:
        return 2

    return 0          




if __name__ == "__main__":
    m = [[1, 2, 1], [0, 2, 1], [1, 0, 2]]
    print("the winer is: ",who_won(m))
