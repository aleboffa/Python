# Write your solution here
def histogram(word):
    groups = {}
    for char in word:
        initial = char
        # initialize when the letter is first encountered
        if initial not in groups:
            groups[initial] = 0 #  key = initial, value = 0
        groups[initial] += 1  #  key=initial, value=value+1

    for key, value in groups.items():
        print(key, value * "*")







if __name__ == "__main__":
    histogram("statistically")