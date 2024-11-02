import random

number=None
count=1

while number !=0:
    number=random.randint(0,10)
    print(f"Number {count} was {number}")
    if number == 7:
        print("Lucky 7!")
    count +=1

