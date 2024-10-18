marks=int(input("Enter marks: "))
if -1 < marks <= 100:
    if marks >= 50:
        print("Pass")
    else:
        print("Weak")
else:
    print("Not a valid mark")
