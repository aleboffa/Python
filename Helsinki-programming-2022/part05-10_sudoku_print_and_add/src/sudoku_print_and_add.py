# Write your solution here
from xml.dom.minidom import Element

def print_sudoku(sudoku: list):
    sep_vert=0
    sep_horiz=1
    element=0
    for row in range(len(sudoku)):
        for col in range(len(sudoku)+2):
            num = sudoku[row][element]
            element += 1
            if sep_vert < 3 and num == 0:
                print("_", end="")
            elif sep_vert < 3 and num != 0:
                print(num, end="")
            else:
                sep_vert = -1
                element -= 1
            print(" ", end="")
            sep_vert += 1
        sep_vert = 0
        print("")
        element=0
        if sep_horiz >= 3:
            print("")
            sep_horiz=0
        sep_horiz += 1    

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

    return sudoku



if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

#    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)