def getItemPrice(message: str):
    value = None
    while(value == None):
        try:
            value = float(input(message))
        except:
            print("Invalid input. Please enter a number.")
    return value

itemList = []

input("Press ENTER to start")
while True:
    itemName = input("Enter Item Name: ")
    itemPrice = getItemPrice(f"Enter Item Price of {itemName}: ")
    itemList.append({"name": itemName, "price": itemPrice})

    command = input("Press Y to add item, or press ENTER to generate the bill")
    if command == "": break

total = 0

print("======= Grocery Bill ========")
for item in itemList:
    print(f"Item: {item["name"]}")
    print(f"Price: {item["price"]} Rs\n")
    total += int(item["price"])

print(f"Total: {total} Rs")
print("======= Thank you for shopping with us ========")