# Write your solution here:
def word_generator(characters: str, length: int, amount: int):
    substring = (characters[i : i + length] for i in range(amount))
    return substring


if __name__=="__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
#####################################################33
#   proffesor solution
#
# from random import choice
 
# def word_generator(letters: str, length: int, amount:int):
#     return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))


####################################################################
#   ejemplo teoria

# substrings = ("abcdefghijklmnopqrstuvwxyz"[i : i + 3] for i in range(24))

# # print out first 10 substrings
# for i in range(10):
#     print(next(substrings))