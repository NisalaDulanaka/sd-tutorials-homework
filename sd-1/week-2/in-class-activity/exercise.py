import random

num=-1
iteration=1

while(num!=0):
    num=random.randint(0,10)
    print(f"The number {iteration} is ",num)
    if num == 7:
        print("Lucky seven")
    iteration +=1
