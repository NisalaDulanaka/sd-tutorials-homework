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


# Tax Calculator Based on Gross Income
"""def calculate_tax():
    gross_income = float(input("Enter your gross income: "))
    tax=0
    if 12500 <= gross_income < 15000:"""


