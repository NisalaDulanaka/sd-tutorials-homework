def is_divisible_by_five(num: int):
    if num % 5 ==0:
        return True
    return False

def is_eligible_to_vote(age: int):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

def num_categorize(num: int):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

def nested_check(num: int):
    if num < 10:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Greater than 10")

def is_leap_year():
    year=int(input("Enter a year: "))
    if year % 4 == 0 or (year % 100 ==0 and year % 400 == 0):
        print("Is a leap year")
    else:
        print("Not a leap year")

def is_vowel():
    char=input("Enter a letter: ")
    vowels = ['a', 'e', 'i', 'o', 'u']

    if char.lower() in vowels:
        print("Is a vowel")
    else:
        print("Is a constant")

def categorize_character():
    character = input("Enter a character: ")
    code=ord(character)
    if 64 < code < 91:
        print("Uppercase")
    elif 96 < code < 123:
        print("Lowercase")
    else:
        print("Special character")

def calculate_discounts(purchased_amount: float):
    if purchased_amount > 1000:
        print("Discount is 10%")
    elif purchased_amount >= 500:
        print("Discount is 5%")
    else:
        print("No discount")


#Hard Exercises

# Tax Calculator Based on Gross Income
def calculate_tax():
    gross_income = float(input("Enter your gross income: "))
    tax=0
    if 12500 < gross_income:
        tax+=(gross_income - 12500) * 20/100
    if 50000 < gross_income:
        tax+=(gross_income - 50000) * 40/100 - (gross_income - 50000) * 20/100
    if 150000 < gross_income:
        tax+=(gross_income - 150000) * 45/100 - (gross_income - 150000) * 40/100
    net_income=gross_income - tax
    print(f"Tax owed {tax} Net income is {net_income}")

def calculate_grade():
    c_score = float(input("Enter your coursework marks: "))
    m_score = float(input("Enter your midterm marks: "))
    f_score = float(input("Enter your final exam marks: "))
    if c_score > 100 or c_score < 0 or m_score > 100 or m_score < 0 or f_score > 100 or f_score < 0:
        print("Invalid score")
        return

    final_score=c_score/100 * 40 + m_score/100 * 25 + f_score/100 * 35

    print(f"final score {final_score}")
    if final_score < 40:
        print("grade F")
    elif final_score < 50:
        print("grade C")
    elif final_score < 70:
        print("grade B")
    else:
        print("grade A")

calculate_grade()
