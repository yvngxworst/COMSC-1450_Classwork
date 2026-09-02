'''
First = input("Enter your first name: ")
Last = input("Enter your last name: ")
print("Hello", Last + ", " + First)


x = 32
y = "Sara"
Z = 3.5

print(type(x))
print(type(y))
print(type(Z))


x = "C:\\Users\\rick\\Documents"


print(x + y)


Length = float(input("Enter the length of the rectangle: "))
Width = float(input("Enter the width of the rectangle: "))
Area = Length * Width
print("The area of the rectangle is", Area)

Name = input("Enter your name: ")
Monthly_Budget = float(input("Enter your monthly budget: "))
Daily_Food_Cost = float(input("Enter your daily food cost: "))
Remaining_Budget = float(Monthly_Budget - (Daily_Food_Cost * 30))
Budget_Summary = "--Budget Summary--\n{Name} | Food Monthly: ${Food_Monthly:.2f} | Remaining: ${Remaining_Budget:.2f}"
print(Budget_Summary.format(Name=Name, Food_Monthly=Daily_Food_Cost * 30, Remaining_Budget=Remaining_Budget))


radius = float(input("What is the radius of the circle? "))
area = 3.14159 * radius ** 2
print("The area of the circle is", area)


Celsius = float(input("Enter the temperature in Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32
print("The temperature in Fahrenheit is", Fahrenheit)


x = input("Enter a number: ")
y = input("Enter another number: ")
z = input("Enter a third number: ")
avg = (float(x) + float(y) + float(z)) / 3
print(avg)


x = input("Enter a number: ")
y = input("Enter another number: ")
print("X is now:", y)
print("Y is now:", x)
'''
original_price = float(input("What is the original price of the item? $"))
discount_percentage = float(input("What is the discount percentage? %"))
sales_tax_percentage = float(input("What is the sales tax percentage? %"))
print("The final price of the item is: $", round(original_price * (1 - discount_percentage / 100) * (1 + sales_tax_percentage / 100), 2))


name = input("What is your name? ")
item_number = int(input("How many items are there? "))
input_price = float(input("What is the price per item in USD? $"))
print("Customer Name:", name)
print("USD Total: $", round(item_number * input_price, 2))
print("Euro Total: €", round(item_number * input_price * 0.91, 2))
print("Service Completed. Thank you for shopping with us!")