# Write your solution to exercise 2 here
def separate_list(numbers: list):
    first = []
    second = []
    for number in numbers:
        if number >= 0:
            first.append(number)
        else:
            second.append(number)

    return first,second

##################################################
if __name__=="__main__":
    numbers = [1, -1, 2, -3, 5, -1, 1, 1, 9]
    numbers1, numbers2 = separate_list(numbers)
    print(numbers1)
    print(numbers2)

    # [1, 2, 5, 1, 1, 9]
    # [-1, -3, -1]