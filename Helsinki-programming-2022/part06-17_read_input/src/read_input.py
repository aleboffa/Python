# Write your solution here
def read_input(text,x,y):
        while True:
            try:
                number = int(input(text))
                if number > x and number < y:
                    return number
            except ValueError:
                pass
            print(f"You must type in an integer between {x} and {y}")

############################
###############################################
if __name__=="__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)