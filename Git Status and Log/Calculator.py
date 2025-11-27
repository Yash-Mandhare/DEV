# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

 # Add this code after 9 step status and law.
def multiply(a, b): 
    return a * b

def main():
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("1) Add")
    print("2) Subtract")
    choice = input("Choose 1 or 2: ").strip()
    if choice == "1":
        print(f"{x} + {y} = {add(x, y)}")
    elif choice == "2":
        print(f"{x} - {y} = {subtract(x, y)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
