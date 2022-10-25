# WRITE YOUR SOLUTION HERE:
class ListHelper:

    def greatest_frequency(my_list: list):
        greatest = 0
        for num in my_list:
            counter = my_list.count(num)
            if counter >  greatest:
                greatest = counter
                numero = num
        return numero

    def doubles(my_list: list):
        greatest = 0
        twice = []
        for num in my_list:
            counter = my_list.count(num)
            if counter >= 2:
                twice.append(num)
        return len(set(twice))

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))