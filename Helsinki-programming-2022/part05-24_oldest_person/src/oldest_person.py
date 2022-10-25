# Write your solution here
def oldest_person(people: list):
    initial=2020
    oldest=0
    for person in people:
        older=person[1]
        if initial > older:
            initial=older
            nombre=person[0]


    return nombre


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))