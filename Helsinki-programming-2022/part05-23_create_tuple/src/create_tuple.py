# Write your solution here
def create_tuple(x: int, y: int, z: int):
    nums=()
    sum=0
    sum = x+y+z
    if x < y and x < z:
        a=x
        if y < z:
            b=z
        else:
            b=y
    elif y < x and y < z:
            a=y
            if x > z:
                b=x
            else:
                b=z
    else:
        a=z
        b=x

    nums=(a,b,sum)    
    
    return nums

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))