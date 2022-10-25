# Write your solution here
def remove_smallest(my_list: list):
    new_list = []
    num=my_list[0]
    for item in my_list:
        if num > item:
            num = item
    my_list.remove(num)




if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)