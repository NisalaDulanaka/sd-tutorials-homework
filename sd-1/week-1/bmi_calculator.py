def main():
    weight=float(input("Weight in kg: "))
    height=float(input("Height in meters: "))

    bmi=weight/(height*height)
    print("Your BMI is: ",bmi)

if __name__ == "__main__":
    main()
