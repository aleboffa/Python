# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest=0
        for line in new_file:  #one number each line as string
            line = line.replace("\n", "")
            if largest < int(line):
                largest=int(line)
    return largest


