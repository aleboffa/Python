# write your solution here
from difflib import get_close_matches


if True:
    # this is never executed
    texto = input("Write text:")

else:
    # hard-coded input
    texto = "This is acually a good and usefull program"

####################################### write your solution here
# create "words" without " " or "\n"
words = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        words.append(line.strip())

# create list single_texto with one single word at a time
single_texto = []
single_texto = texto.split(" ")

# process
text_output = "" # text output
for ind_word in range(0,len(single_texto)):
    if single_texto[ind_word].lower() in words:
        text_output += single_texto[ind_word] + " "
    else:
        text_suger = single_texto[ind_word]
        text_output += "*" + single_texto[ind_word] + "*" + " "

print(text_output)
print(get_close_matches(text_suger, words))