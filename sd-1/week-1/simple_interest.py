def main():
    principal=float(input("Enter principal amount: "))
    rate=float(input("Enter rate of interest(annual): "))
    time=int(input("Enter number of years: "))

    interest=principal * rate * time
    print(f"Your interest is {interest} .rs")

if __name__ == "__main__":
    main()