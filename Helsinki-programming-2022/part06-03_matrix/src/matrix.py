# write your solution here
def matrix_sum():
    with open("matrix.txt") as new_file:
        suma=0
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")  # list numbers as str
            new_list = [int(x) for x in numbers] # transform numbers list from str to int
            for num in new_list:
                suma =suma + num
    return suma
    
    
def matrix_max():
    with open("matrix.txt") as new_file:
        greater=0
        greatest=greater
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            new_list = [int(x) for x in numbers] # transform numbers list from str to int
            greater = max(new_list)
            if greater > greatest:
                greatest = greater
    return greatest


def row_sums():
    with open("matrix.txt") as new_file:
        list_sum_row=[]
        sum_row=0
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            new_list = [int(x) for x in numbers] # transform numbers list from str to int
            sum_row = sum(new_list)
            list_sum_row.append(sum_row)

    return list_sum_row

