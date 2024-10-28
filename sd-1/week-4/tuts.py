# printing numbers with a for loop
for i in range(1,6):
    print(i)

count=5
while count > 0:
    print(count)
    count-=1

count=0
value=1
while value <= 5:
    count += value
    value += 1
print(count)

even_count=0
for i in range(2,11,2):
    even_count += i
print(even_count)

input_num=0
while input_num >= 0:
    input_num = int(input("Enter a number: "))
print("program ended")

number=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")

num=int(input("Enter number to count factorial: "))
fact=num
while num > 1:
    num -= 1
    fact *= num
    print(fact)
print(f"Factorial is {fact}")

skip=False
for i in range(2,20):
    for j in range(2,i):
        if i % j == 0:
            skip=True
            break
        else:
            skip=False
    if skip != True:
        print(i)

for r in range(5):
    for c in range(r+1):
        print(f"{r +1}",end="")
    print()
