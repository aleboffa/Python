# Write your solution here
from unittest import result


def smallest_average(person1: dict, person2: dict, person3: dict):

    sum1=person1["result1"]+person1["result2"]+person1["result3"]
    sum2=person2["result1"]+person2["result2"]+person2["result3"]
    sum3=person3["result1"]+person3["result2"]+person3["result3"]

    if sum1 < sum2 and sum1 < sum3:
        return person1
    elif sum1 > sum2 and sum2 < sum3:
        return person2
    else:
        return person3





#   person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
#   person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
#   person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

#   print(smallest_average(person1, person2, person3))

#   {'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}
