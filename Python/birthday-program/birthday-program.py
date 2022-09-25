class BirthdayProgram:

    thisYear = 2022

    name = input("Please enter your name: ")
    age = int(input("Please enter your year of birth: "))
    choice = int(input("Do you already had birthday this year? 1: Yes, 2: no "))

    if choice == 1:
        age = thisYear - age
        print("Hello " + name + "," + " you are " + str(age) + " years old")
    else:
        age = thisYear - age - 1
        print("Hello " + name + "," + " you are still " + str(age) + " years old")

