
# check row
def row_correct(sudoku: list, row_no: int):
    row=sudoku[row_no]
    for square in row:
        if square != 0:
            count=row.count(square)
            if count > 1:
                return False
            
    return True

# check column
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

# check block
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
#############################    
#############################
# Write your solution here
def sudoku_grid_correct(sudoku: list):
    row=0
    flag= False
    while row <= 8:   ### check rows
        if not row_correct(sudoku, row) or row > 8:
            flag = False
            break
        else:
            row += 1
            flag = True

    if flag:
        col =0
        while col <= 8:   ### check cols
            if not column_correct(sudoku, col) or col > 8:
                flag = False
                break
            else:
                col += 1
                flag = True
        if flag:
            block =0
            rows=[0,3,6]
            cols=[0,3,6]
            for row in rows: 
                if flag:
                    for col in cols:
                        block += 1
                        if not block_correct(sudoku, row, col):
                            flag = False
                            break
                        else:
                            flag = True
            if not flag:
                return False
            else:
                return True

        else:
            return False
    else:
        return False
################################            



if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

#    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

#    print(sudoku_grid_correct(sudoku2))

    sudoku = [
    [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
    [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
    [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
    [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
    [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
    [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
    [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
    [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
    [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],
    ]
#    print(sudoku_grid_correct(sudoku))

    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku))