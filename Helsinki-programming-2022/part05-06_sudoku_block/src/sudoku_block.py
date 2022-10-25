# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    new_matrix=[]
    for row in range(row_no, row_no + 3):
        for col in range(column_no, column_no + 3):
            square= sudoku[row][col]
            new_matrix.append(square)

    for square in new_matrix:
        if square != 0:
            count=new_matrix.count(square)
            if count > 1:
                return False
            
    return True



if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 2, 0, 0, 0, 0, 4, 0, 4],
    [2, 9, 4, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 5, 6, 0],
    [7, 0, 5, 7, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 1, 2))