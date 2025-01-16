import time

def main_menu():
    print("\n+. For Add")
    print("-. For Subtraction")
    print("*. For Multiplication")
    print("/. For Division")
    print("%. For Modulo")
    print("@. For history")
    print("Enter 'quit' to end the program")
    
def history(num1, num2, result, choice):
    with open("history.txt", "a") as my_file:
        my_file.write(str(num1) + " " + choice + " " + str(num2) + " = " + str(result) + "\n")

def timer():
    time.sleep(1)
    print("\n--------------------------------------------------------------------------")    

def calculator(): 
    while True:
        main_menu()
        choice = input("Choose your operation: ")
        
        if choice == "quit":
            print("Goodbye!")
            break
        elif choice == "@":
            try:
                with open("history.txt", "r") as my_file:
                    print("\nHistory of calculations:")
                    print(my_file.read())
            except FileNotFoundError:
                print("No history available.")
            continue
        elif choice in ["+", "-", "*", "/", "%"]:
            try:
                num1 = float(input("Enter a number: "))
                num2 = float(input("Enter another number: "))
                
                if choice == "+":
                    result = num1 + num2
                elif choice == "-":
                    result = num1 - num2
                elif choice == "*":
                    result = num1 * num2
                elif choice == "/":
                    try:
                        result = num1 / num2
                    except ZeroDivisionError:
                        print("Error: Division by zero")
                        continue
                elif choice == "%":
                    result = num1 % num2

                print(f"{num1} {choice} {num2} = {result}")
                history(num1, num2, result, choice)
                timer()

            except ValueError:
                print("Invalid number. Please try again.")
        else:
            print("Invalid input. Please choose a valid operation.")
            
calculator()
