units = ["KILOMETERS","MILES","METERS"]

def convertDistance(numInput: float, fromUnit: str, toUnit: str):
    if fromUnit == units[0]:
        if toUnit == units[1]:
            return numInput *  0.621371
        elif toUnit == units[2]:
            return numInput * 1000
    elif fromUnit == units[1]:
        if toUnit == units[0]:
            return numInput * 1.609344
        elif toUnit == units[2]:
            return numInput * 1,609.344
    elif fromUnit == units[2]:
        if toUnit == units[0]:
            return numInput/1000
        elif toUnit == units[1]:
            return numInput * 0.000621371
    
    return numInput

distance = None; fromUnit = None; toUnit = None
while distance is None:
    try:
        distance = float(input("Enter distance"))
    except:
        print("Invalid input. Please enter a number.")

while True:
    fromUnit = input("Enter unit of distance (KILOMETERS, MILES, METERS)")
    if fromUnit in units: break

while True:
    toUnit = input("Enter unit to be converted to (KILOMETERS, MILES, METERS)")
    if toUnit in units: break

print(f"Distance is {convertDistance(distance, fromUnit, toUnit)} {toUnit}")