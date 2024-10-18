import math

def grade_calculator():
    tot_marks=0
    for i in range(0,5):
        grade = int(input(f"Enter grade for student {i+1}: "))
        tot_marks += grade
    
    avg = tot_marks / 5
    print(f"Average is {avg}")
    if avg >= 75:
        print("Grade: A")
    elif avg >= 65:
        print("Grade B")
    elif avg >= 55:
        print("Grade C")
    elif avg >= 35:
        print("Grade S")
    else:
        print("Grade F")

def savings_goal_tracker():
    target_goal=float(input("Enter the target saving amount: "))
    current_amount=float(input("Enter current savings amount: "))
    monthly_amount=float(input("Enter monthly savings amount: "))

    months=(target_goal - current_amount) / monthly_amount
    print(f"Number of months to reach the target is {months}")

def distance_between_points():
    x1=int(input("Enter x coordinate of point 1: "))
    y1=int(input("Enter y coordinate of point 1: "))
    x2=int(input("Enter x coordinate of point 2: "))
    y2=int(input("Enter x coordinate of point 2: "))

    distance=math.sqrt((x2 -x1)**2 + (y2 - y1)**2)
    print(f"The distance between the two points is {distance}")

functions=[grade_calculator,savings_goal_tracker,distance_between_points]
print(f"\n\nThe list of available functions")
print("1.grade_calculator")
print("2.savings_goal_tracker")
print("3.distance_between_points")
function_number=int(input("Enter the function number you want to call: "))
print(f"Executing function....\n")
functions[function_number - 1]()
