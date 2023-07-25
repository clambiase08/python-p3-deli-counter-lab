katz_deli = []


def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for person in range(len(katz_deli)):
            message += f" {person + 1}. {katz_deli[person]}"
        print(message)


def take_a_number(katz_deli, person):
    katz_deli.append(person)
    print(f"Welcome, {person}. You are number {katz_deli.index(person) + 1} in line.")


def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
