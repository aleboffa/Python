# Write your solution here
def transpose(my_list: list):
    new_list = []

    # para cpiar listas anidadas o arrays hacer asi
    for r in my_list:         # r es row (fila)      
        new_list.append(r[:]) # agrega toda la fila(row)
    # fin copia matriz
    #     

    # copy items from the new list into the old list
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            my_list[i][j] = new_list[j][i]
    print("new ", new_list)
    print("orig ", my_list)

    #############################
    #  solucion profesor
    # 
#     def transpose(matrix: list):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i, n):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = temp
 
#             #..or alternatively
#             # matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    
if __name__ == "__main__":
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print(matrix)
    
    print()
    m1=transpose(matrix)
 
    