
def filter_incorrect():
    with open("lottery_numbers.csv") as my_file:
        correcto=[]
        grabar=True
        result=0
        for line in my_file:
            grabar=True
            parts = line.split(';')
            print("parts: ",parts)
            # validate week   week[0]="week"  week[1]=1 a 100?
            week = parts[0].split(" ")
            lista_numeros_str = list(str(range(1,100)))
            if week[1].isdigit()== False :
                grabar =False
                print("no correct week")
                continue
            if int(week[1]) not in range(1,100):
                grabar = False
                print("number not in 1-39")
                continue

            # validate numeros   week[1]=7 numeros del 1 al 39
            parts[1]=parts[1].strip()
            numeros = parts[1].split(",")
#            print(numeros)
            if len(numeros) < 7:    #   error cant numbers < 7
                grabar = False
                print(" no 7 num", len(num))
                continue

            for num in numeros:
                print("numero; ",num)
                if not num.isdigit():
                    grabar = False
                    print("no digit 1",num)
                    break
                if int(num) not in range(1,39):
                    grabar = False
                    print("no range")
                    break

                if numeros.count(num) > 1:
                    grabar = False  
                    print("repetido",num)      
                    break    
            if grabar:
                correcto.append(parts)
                print("grabado: ",correcto)

    with open("correct_numbers.csv", "w") as my_file:
        for linea in correcto:

            texto = f"{linea[0]};{linea[1]}"
#            print(texto)
            my_file.write(texto + "\n")

###############################################
if __name__=="__main__":
    filter_incorrect()


##########################################
#####
#####  solucion profesor
#####
##########################################
# def filter_incorrect():
#     with open("lottery_numbers.csv") as input_file, open("correct_numbers.csv", "w") as result_file:
#         for row in input_file:
#             parts = row.strip().split(";")
#             if len(parts) != 2:
#                 continue
#             week = parts[0].split(" ")
#             error = False
#             if len(week) != 2 or week[0] != "week":
#                 error = True
#             try:
#                 mika = int(week[1])
#             except:
#                 error = True
#             number_list = parts[1].split(",")
#             if len(number_list) != 7:
#                 error = True
 
#             # numbers already listed --> to find out duplicates
#             listed = []
#             for item in number_list:
#                 try:
#                     number = int(item)
#                     if number < 1 or number > 39 or number in listed:
#                         error = True
#                     listed.append(number)
#                 except:
#                     error = True
#             if not error:
#                 result_file.write(row)