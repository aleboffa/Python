# Write your solution here
def dict_of_numbers():
    new_dict={}
    item=""
    new_dict[0]="zero"
    new_dict[1]="one"
    new_dict[2]="two"
    new_dict[3]="three"
    new_dict[4]="four"
    new_dict[5]="five"
    new_dict[6]="six"
    new_dict[7]="seven"
    new_dict[8]="eight"
    new_dict[9]="nine"
    new_dict[10]="ten"
    new_dict[11]="eleven"
    new_dict[12]="twelve"
    new_dict[13]="thirteen"
    new_dict[14]="fourteen"
    new_dict[15]="fifteen"
    new_dict[16]="sixteen"
    new_dict[17]="seventeen"
    new_dict[18]="eighteen"
    new_dict[19]="nineteen"
    new_dict[20]="twenty"
    new_dict[30]="thirty"
    new_dict[40]="forty"
    new_dict[50]="fifty"
    new_dict[60]="sixty"
    new_dict[70]="seventy"
    new_dict[80]="eighty"
    new_dict[90]="ninety"
    for i in range(21,100):
        if i >= 21 and i <= 29:
            item = "twenty"+"-"+new_dict[i-20]
        if i >= 31 and i <= 39:
            item = "thirty"+"-"+new_dict[i-30]
        if i >= 41 and i <= 49:
            item = "forty"+"-"+new_dict[i-40]
        if i >= 51 and i <= 59:
            item = "fifty"+"-"+new_dict[i-50]
        if i >= 61 and i <= 69:
            item = "sixty"+"-"+new_dict[i-60]
        if i >= 71 and i <= 79:
            item = "seventy"+"-"+new_dict[i-70]
        if i >= 81 and i <= 89:
            item = "eighty"+"-"+new_dict[i-80]
        if i >= 91 and i <= 99:
            item = "ninety"+"-"+new_dict[i-90]

        new_dict[i]=item
        item=""
    new_dict[0]="zero"
    new_dict[1]="one"
    new_dict[2]="two"
    new_dict[3]="three"
    new_dict[4]="four"
    new_dict[5]="five"
    new_dict[6]="six"
    new_dict[7]="seven"
    new_dict[8]="eight"
    new_dict[9]="nine"
    new_dict[10]="ten"
    new_dict[11]="eleven"
    new_dict[12]="twelve"
    new_dict[13]="thirteen"
    new_dict[14]="fourteen"
    new_dict[15]="fifteen"
    new_dict[16]="sixteen"
    new_dict[17]="seventeen"
    new_dict[18]="eighteen"
    new_dict[19]="nineteen"
    new_dict[20]="twenty"
    new_dict[30]="thirty"
    new_dict[40]="forty"
    new_dict[50]="fifty"
    new_dict[60]="sixty"
    new_dict[70]="seventy"
    new_dict[80]="eighty"
    new_dict[90]="ninety"
    print(new_dict[40]+ "  segundo")
    return new_dict


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
  
#    two
#    eleven
#    forty-five
#    ninety-nine
#   zero