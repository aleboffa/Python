# Write your solution here
def prime_numbers():
    number = 2
    try:
        for x in range(2,number-1):
            if number%x == 0 or number%2 == 0 or number%3 == 0:
                number += 1
                continue
            else:
                yield number
                number += 1
    except StopIteration:
        print("chau")


if __name__=="__main__":
    numbers = prime_numbers()
    for i in range(20):
        print(next(numbers))