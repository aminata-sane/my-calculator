# ---------------1. Easy math calculations------------------
def operation_mat():
    try:
        while True:
            try:
                num1 = float(input("Write your first number: "))
                num2 = float(input("Write your second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            operation = input("Write your operation: ")


            # The users choise

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("The answer will be always 0")
                    continue
                result = num1 / num2
            elif operation == "%":
                result = num1 / 100 * num2
            else:
                print("Error. Invalid operation")
                continue
            # -------------------2. calculation  of three or more operations
            #--------------------3. Save result to history------------------

            with open('history.txt', 'a') as history:
                history.write(f'{num1} {operation} {num2} = {result}\n')

            if result.is_integer():  
                print(f"Result: {int(result)}")
            else:  
                print(f"Result: {result}")
    except KeyboardInterrupt:
        print("Return: ")
            # -------------------5. Graphical interface---------------------
            
            # -----------------Menu------------------
def main():
        while True:
            print("\nMenu:")
            print("Easy math calculations - press 1: ")
            print("Difficult math calculations - press 2: ")
            print("See the history - press 3: ")
            print("Delate history - press 4: ")
            print("To watch the interface graphique - press 5: ")
            print("Exit - press 6: ")

            choise = input ("Make your choice: ")    

            if choise == "1":
                operation_mat()
            elif choise == "2":
                print("Difficult math calculations")
            elif choise == "3":
                # Open file in read mode to display history
                with open('history.txt', 'r') as history_file:
                    print("Calculation History:")
                    print(history_file.read())
            elif choise == "4":
                # delate history
                with open('history.txt', 'w') as history_file:
                    history_file.truncate(0)
                    print("History deleted.")
            elif choise == "5":
                print("Graphical interface")
            elif choise == "6":
                print("Exit")
            else:
                print("Invalid choice. Please try again.")
main()

    

