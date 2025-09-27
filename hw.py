try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    age = -1 

if age > 0: 
    if age % 2 == 0:
        print("Your age is an Even number.")
    else:
        print("Your age is an Odd number.")
elif age == 0: 
    print("Age cannot be zero.")
elif age < 0 and age != -1: 
    print("Age cannot be negative.")
