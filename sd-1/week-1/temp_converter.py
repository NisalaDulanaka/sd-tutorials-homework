def convertTemp(temp: float, toCelcius=False):
    if toCelcius:
        convertedTemp = (temp - 32) * (5/9)
    else:
        convertedTemp = temp * (9/5) +32
    return convertedTemp
temp = None; convertTo = None
while(temp == None):
    try:
        temp = float(input("Enter the temperature: "))
    except:
        print("Invalid input. Please enter a number.")

while(convertTo == None):
    tempValue = input("Which unit do you want to convert it to? (F for farientheight, C for celsius): ")
    if (tempValue == "C" or tempValue == "F"):
        convertTo = tempValue
    else:
        print("Invalid input. Only 'F' and 'C' are allowed\n")

print("Temperature is {} {}".format(
    convertTemp(temp, convertTo == "C"),
    "c" if convertTo == "Celsius" else "fahrenheit"
))