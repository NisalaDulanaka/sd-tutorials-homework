import random
#Generate a random number ten times and each time check if it is 7, and print luck 7, otherwise print the number

for i in range(10):
    random_num=random.randint(0,10)
    if(random_num == 7):
        print("Luck 7")
    else:
        print(random_num)


