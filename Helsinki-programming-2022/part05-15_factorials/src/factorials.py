# Write your solution here
def factorials(n: int):
    fact = 1
    dict_fact = {}
 
    for i in range(1,n+1):
        fact = fact*i
        dict_fact[i] = fact
        
    return dict_fact
    



if __name__ == "__main__":

    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])

#    1
#    6
#    120