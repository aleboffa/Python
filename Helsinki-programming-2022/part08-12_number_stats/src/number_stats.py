# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.each_number =[]

    def add_number(self, number:int):
        self.numbers += 1
        self.each_number.append(number)

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        if self.numbers > 0:
            return sum(self.each_number)
        else:
            return 0

    def average(self):
        if self.numbers > 0:
            return sum(self.each_number)/self.numbers
        else:
            return 0 

print("Please type in integer numbers:")
stats = NumberStats()
even = NumberStats()    # par
odd = NumberStats()     # impar

while True:
    code = int(input())
    if code == -1:
        break
    stats.add_number(code)
    if code % 2 == 0:
        even.add_number(code)
    else:
        odd.add_number(code)


print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())




