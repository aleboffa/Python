# Write your solution here

where = "diary.txt"

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    selection = input("Function:")
    if selection == "1":
        texto = input("Diary entry: ")
        with open(where, "a") as my_file:
            my_file.write(texto+"\n")
        print("Diary saved")
        print()
    
    elif selection == "2":
        print("Entries: ")
        new_file = []
        with open(where) as my_file:
            for line in my_file:
                new_file = line.strip()
                print(new_file)
 
    else:
        print("Bye now!")
        break
    