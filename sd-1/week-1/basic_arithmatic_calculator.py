def add(n1: int, n2: int):
    return n1 + n2

def subtract(n1: int, n2: int):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    #Take number inputs
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    #Take the operator input
    operation = input("Enter the operation: ")
    if operation not in operations:
        print("Invalid operation")
        return
    
    result = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
    

if __name__ == "__main__":
    main()
