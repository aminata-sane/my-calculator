import os
import json

def main_menu():
    print("\n+. For Add")
    print("-. For Subtraction")
    print("*. For Multiplication")
    print("/. For Division")
    print("%. For Modulo")
    print("@. For history")
    print("Enter 'quit' to end the program")

# Check or initialize the JSON file
if not os.path.exists("history.json"):
    with open("history.json", "w") as file: 
        json.dump({"calculations": []}, file)  # Initialize with an empty structure

def write_json(num1, choice, num2, result):
    with open("history.json", "r+") as file:
        data = json.load(file)  # Load the existing data
        data["calculations"].append({
            "choice": choice,
            "num1": num1,
            "num2": num2,
            "result": result
        })
        file.seek(0)
        json.dump(data, file, indent=4)  # Save new data

def read_history():
    with open("history.json", "r") as file:
        data = json.load(file)
        if data["calculations"]:
            for calc in data["calculations"]:
                print(f"{calc['num1']} {calc['choice']} {calc['num2']} = {calc['result']}")
        else:
            print("No calculations found in history.")

def calculator(): 
    while True:
        main_menu()
        choice = input("Choose your operation: ")
        
        if choice == "quit":
            print("Goodbye!")
            break
        elif choice == "@":
            read_history()
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
                write_json(num1, choice, num2, result)
              
            except ValueError:
                print("Invalid number. Please try again.")
        else:
            print("Invalid input. Please choose a valid operation.")

calculator()
