
def simple_calculation ():
    print("Choose your option")
    print("1. Addition - press 1")
    print("2. Substraction - press 2")
    print("3. Multiplication - press 3")
    print("4. Division - press 4")
    print("5. Finish - press 5")

    try:
        while True:
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))
            except:
                print("Error")
            
            operation = int(input("Make your choise 1-5: "))

            if operation == 1:
                result = num1+num2
            elif operation == 2:
                result = num1-num2
            elif operation == 3:
                result = num1*num2
            elif operation == 4:
                result = num1/num2
            elif operation == 5:
                break
            else:
                print("Invalid chose. Try again: ")
            
            if result.is_integer():
                print(f"Result is {int(result)}.")
            else:
                print(f"Result is {result}.")

            with open('history.txt', 'a') as history:
                history.write(f'{num1} {operation} {num2} = {result}\n')
    except KeyboardInterrupt:
        print("Return: ")







def main_menu():
    print("\nMenu: ")
    print("1.Calculator simple - press 1")
    print("2.Camculator with few options - press 2")
    print("3.Show history - press 3")
    print("4.Delate history - press 4")
    print("5. Finish - press 5")

    while True:
        choise = int(input("Choose your option 1-5: "))
        if choise == 1:
            simple_calculation()
        elif choise == 2:
            print()
        elif choise == 3:
            with open('history.txt', 'r') as history_file:
                print("Calculation History:")
                print(history_file.read())
        elif choise == 4:
            with open('history.txt', 'w') as history_file:
                history_file.truncate(0)
                print("History deleted.")
        elif choise == 5:
            break
        else:
            print("Invalid choise. Try again: ")
main_menu()