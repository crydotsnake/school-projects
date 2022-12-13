import os
import sys

thisYear = int(input("Please enter the current year "))
name = input("Please enter your name: ")
age = int(input("Please enter your year of birth: "))
choice = str(input("Do you already had birthday this year? yes/no "))

if choice == "yes":
    age = thisYear - age
    print("Hello " + name + "," + " you are " + str(age) + " years old")
else:
    age = thisYear - age - 1
    print("Hello " + name + "," + " you are still " + str(age) + " years old")

askAgainMessage = str(input("Would you like to ask another person? yes/no "))

if askAgainMessage == "yes":
    os.execv(sys.executable, ['python'] + sys.argv)
else:
    print("Good Bye!")
