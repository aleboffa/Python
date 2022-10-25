# Write your solution here
import copy

def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for character in row:
            s += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if s%3 == 0 and s < 8:
                m += " "
            print(m, end="")
 
        print()
        r += 1
        if r%3 == 0 and r < 8:
            print()
 
def copy_and_add(list_a: list, row_no: int, column_no: int, number: int):
    new_list=copy.deepcopy(list_a)

    print()
    new_list[row_no][column_no] = number
    return new_list
##############################
## professor solution
#
# def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
#     new_list = []
#     for r in sudoku:
#         new_list.append(r[:])
 
#     new_list[row_no][column_no] = number
#     return new_list
# # Write your solution here

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
    grid_copy = copy_and_add(sudoku,0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)