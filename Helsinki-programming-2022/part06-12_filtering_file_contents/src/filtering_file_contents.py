# Write your solution here
def filter_solutions():
    with open("solutions.csv") as my_file:
        correcto=[]
        incorrecto=[]
        operacion=[]
        result=0
        for line in my_file:
            parts = line.split(';')
            if "+" in parts[1]:
                operacion = parts[1].split("+")
                result = int(operacion[0]) + int(operacion[1])
            else:
                operacion = parts[1].split("-")
                result = int(operacion[0]) - int(operacion[1])
            if int(parts[2]) == result:
                correcto.append(parts)
            else:
                incorrecto.append(parts)
    with open("correct.csv", "w") as my_file:
        for linea in correcto:
            texto = f"{linea[0]};{linea[1]};{linea[2]}"
            my_file.write(texto)

    with open("incorrect.csv", "w") as my_file:
        for linea in incorrecto:
            texto = f"{linea[0]};{linea[1]};{linea[2]}"
            my_file.write(texto)

###############################################
if __name__=="__main__":
    filter_solutions()

#  Arto;2+5;7
#  Pekka;3-29;1 

