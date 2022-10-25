# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
#   id;first;last
#   12345678;peter;pythons

    exercise_data = "exercises1.csv"
#   id;e1;e2;e3;e4;e5;e6;e7
#   12345678;4;1;1;4;5;2;4

######################################

names = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1].strip() + " " + parts[2].strip()

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exercises[parts[0]] = int(parts[1])+int(parts[2])+int(parts[3])+int(parts[4])+int(parts[5])+int(parts[6])+int(parts[7])

for id, name in names.items():
    if id in exercises:
        total_exerc=exercises[id]
        print(name,total_exerc)
