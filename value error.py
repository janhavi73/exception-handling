try:
    number=int(input("please enter an number: "))
    print(number, "is your number")

except ValueError as ex:
    print(ex)    