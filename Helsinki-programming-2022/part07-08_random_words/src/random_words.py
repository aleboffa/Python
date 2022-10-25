import random

def words(n: int, beginning: str):
    file = "words.txt"
    lista = []
    lista_final = []
    lista3 = []
    words = []
    with open(file) as new_file:
        for line in new_file:
            words.append(line.strip())

    for word in words:
        if word.startswith(beginning):
            if word in lista:
                continue
            lista.append(word)

    lista_final = random.choices(lista,k=n)

    if len(lista_final) < n:
        raise ValueError(" too few words")
    lista3 = sorted(lista_final)

    anterior = ""
    for word in lista3:
        if word == anterior:
            raise ValueError(" repetidas")            
        else:
            anterior = word

    return lista3



if __name__=="__main__":
    word_list = words(30, "car")
    for word in word_list:
        print(word)