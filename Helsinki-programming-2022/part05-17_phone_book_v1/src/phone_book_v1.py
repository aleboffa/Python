# Write your solution here
book={}
name=""
number=""
while True:
    comando = int(input("command (1 search, 2 add, 3 quit): "))
    if comando == 1:
        name = input("name: ")
        if name in book:
            print(book[name])
        else:
            print("no number")
    elif comando == 2:
        name = input("name: ")
        number = input("number: ")
        book[name]=number
        
        print("ok!")
    elif comando == 3:
        print("quitting...")
        break    