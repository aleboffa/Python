# Write your solution here
def column_correct(sudoku: list, column_no: int):
    col=[]
    for row in sudoku:
        col.append(row[column_no])
    for square in col:
        if square != 0:
            count=col.count(square)
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

#   print(column_correct(sudoku, 0))
#    print(column_correct(sudoku, 1))
    print(column_correct(sudoku, 2))