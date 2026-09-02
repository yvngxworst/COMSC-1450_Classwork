'''
number = int(input("Enter a positive or negative number: "))
if number > 0:
    print("The number is positive.")
if number < 0:
    print("The number is negative.")

number = int(input("Enter a even or odd number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

age = int(input("How old are you? "))
if age <= 19 and age >= 13:
    print("You are a teenager.")
else:
    print("You are not a teenager.")


Temperature = float(input("What is the temperature? "))
if Temperature >= 80:
    print("It is hot outside.")
if Temperature < 80 and Temperature >= 60:
    print("It is warm outside.")
if Temperature < 60 and Temperature >= 32:
    print("It is cold outside.")


number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))
if number_1 > number_2:
    print(number_1, "is greater than", number_2)
if number_1 < number_2:
    print(number_1, "is less than", number_2)
if number_1 == number_2:
    print(number_1, "is equal to", number_2)


x = int(input("Enter your age: "))
if x >=13 and x <=19:
    print("You are a teenager.")
if x < 13 or x > 19:
    print("You are not a teenager.")


number = int(input("Enter a number: "))
if number >=0 and number <=100:
    print("The number is valid.")
else:
    print("The number is invalid.")


number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))
if number_1 == number_2:
    print("They are equal.")
else:
    print("They are not equal.")


password = input("Enter the password: ")
if password == "1234":
    print("Access granted.")
else:
    print("Access denied.")


temperature = float(input("What is the temperature? "))
if temperature >100:
    print("Very hot outside.")
elif temperature >80 and temperature <=100:
    print("Hot outside.")
elif temperature >60 and temperature <=80:
    print("Warm outside.")
else:
    print("Cold outside.")


grade = int(input("Enter your grade: "))
if grade >= 90:
    print("You got an A.")
if grade >= 80 and grade < 90:
    print("You got a B.")
if grade >= 70 and grade < 80:
    print("You got a C.")
if grade >=60 and grade < 70:
    print("You got a D.")
if grade < 60:
    print("You got an F.")


number_one = int(input("Enter a number: "))
number_two = int(input("Enter another number: "))
number_three = int(input("Enter a third number: "))
if number_one > number_two and number_one > number_three:
    print(number_one, "is the largest number.")
if number_two > number_one and number_two > number_three:
    print(number_two, "is the largest number.")
if number_three > number_one and number_three > number_two:
    print(number_three, "is the largest number.")


age = int(input("How old are you? "))
if age < 13:
    print("Your ticket price is $5.")
if age >= 13 and age <= 17:
    print("Your ticket price is $7.")
if age >= 18 and age < 65:
    print("Your ticket price is $12.")
if age > 65:
    print("Your ticket price is $7.")
'''

print("Welcome to the Calculator!")
number_one = int(input("Enter a number: "))
number_two = int(input("Enter another number: "))
operation = input("Enter an operation (+, -, *, /): ")
if operation == "+":
    print(number_one, "+", number_two, "=", number_one + number_two)
if operation == "-":
    print(number_one, "-", number_two, "=", number_one - number_two)
if operation == "*":
    print(number_one, "*", number_two, "=", number_one * number_two)
if operation == "/":
    print(number_one, "/", number_two, "=", number_one / number_two)