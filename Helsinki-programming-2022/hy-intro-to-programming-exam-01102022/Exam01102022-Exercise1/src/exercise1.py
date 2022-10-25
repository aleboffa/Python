# Write your solution to exercise 1 here

total = 0
print(total)
while True:
    option = input("Type in a calculation or quit: ")
    if option.lower() == "quit":
        break
    operator = option[0]        # "-" or "+"
    number = int(option[1:])    # 30 integer like example, not float
    if operator == "+":
        total += number
    else:
        total -= number
    print(total)

#######################################
#  output
#######################################
# 0
# Type in a calculation or quit: -30
# -30
# Type in a calculation or quit: +25
# -5
# Type in a calculation or quit: quit