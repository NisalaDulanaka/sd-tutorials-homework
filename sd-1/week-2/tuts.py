import math

#Calculate Expressions
print("8+2*5 = ", (8 + 2 *5))
print("(8 + 2) *5 = ", ((8 + 2) *5))
print("20/4 = ", (20/4))
print("20//3 = ", (20//3))
print("20%3 = ", (20%3))
print("20**3 = ", (20**3))

# Variable Assignments
a = 10 +5
print("a=",a)
b = 30
print("b=", b)
b+=5
print("b=", b)

# Arithmatic Assignment Operators
x=10
print("Add 5 to x", x +5)
print("Multiply x by 3", x *3)
print("Substract 2 from x",x-2)
x=x//4
print("Divide x by 4 and update x with the quotient",x)

#Data types
print(" type of 42",type(42))
print(" type of 3.14",type(3.14))
print(" type of True",type(True))
print(" type of 'Hellow, world'",type("Hello, World"))

#Type casting
print("Converts the string '123' to an integer and adds 10 to it",int("123") + 10)
print("Converts the number 50 to a string and concatenates it with ' apples'.",str(50) + "apples")
print("Convert 3.9 to an integer",int(3.9))

#Area of a Circle Calculator
def area_of_circle():
    radius=float(input("Enter radius: "))

    area=math.pi * radius * radius
    print("The area of the circle is: ", area)

#Salary Increase Calculator
def salary_increase_calculator():
    current_salary=float(input("Enter current salary: "))
    increase_perc=float(input("Enter increase percentage: "))

    new_salary= current_salary + (current_salary * increase_perc/100)
    print(f"The new salary is {new_salary}")

#Volume of a Cylinder Calculator
def volume_of_cylinder_calculator():
    radius=float(input("Enter radius: "))
    height=float(input("Enter height: "))

    volume=math.pi * radius * radius * height
    print("The volume of the cylinder is: ", volume)

#Cuboid Area, Perimeter, and Volume Calculator
def cuboid_area_perimeter_volume_calculator():
    length=float(input("Enter the length: "))
    height=float(input("Enter the height: "))
    width=float(input("Enter the width: "))

    base_area=length * width
    volume=base_area * height
    perimeter=(length + width) * 2 
    print("The base area of the cube is: ", base_area)
    print("Perimeter :", perimeter)
    print("The volume of the cube is: ", volume)

functions=[area_of_circle,salary_increase_calculator,volume_of_cylinder_calculator,cuboid_area_perimeter_volume_calculator]
print("The list of available functions")
print("1.area_of_circle")
print("2.salary_increase_calculator")
print("3.volume_of_cylinder_calculator")
print("4.cuboid_area_perimeter_volume_calculator")
function_number=int(input("Enter the function number you want to call: "))
functions[function_number - 1]()








