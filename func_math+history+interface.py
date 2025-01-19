from tkinter import *
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

            # display integer or decimal
            if result.is_integer():  
                print(f"Result: {int(result)}")
            else:  
                print(f"Result: {result}")
                
    except KeyboardInterrupt:
        print("Return: ")
# -------------------5. Graphical interface---------------------
def launch_gui():
    tk=Tk()
    tk.geometry("260x370")
    ent = Entry()

    ent=Entry(tk, font=("Arial", 14), justify="right" )
    ent.place(x=20, y=20, width=220, height=30)

    
    # buttons C and =
    # C
    def button_C_click():
        ent.delete(0, END)
    button_C = Button(text="C", font="14", command=button_C_click)
    button_C.place(x=20, y=70, width=100, height=40)
    # =
    def equal_click():
        try: 
            c = float(ent.get())
            global a,b 
            ent.delete(0, END)

            if b =="+":
                result = a + c
            elif b =="-":
                result = a - c
            elif b == "*":
                result = a * c
            elif b == "/":
                if c == 0:
                    ent.insert(END, "Error")
                    return
                result = a / c

            # Save history
            with open('history.txt', 'a') as history:
                history.write(f'{a} {b} {c} = {result}\n')
                
            ent.insert(END, result)
        except ValueError:
            ent.insert(END, "Error")

    equal = Button(text="=", font="14", command = equal_click)
    equal.place(x=140, y=70, width=100, height=40)

    # buttons 0-9
    # 0
    def b0_click():
        ent.insert(END, "0")
    b0 = Button(text="0", font="14", command=b0_click)
    b0.place(x=20, y=310, width=100, height=40)
    # 1
    def b1_click():
        ent.insert(END, "1")
    b1 = Button(text="1", font="14", command=b1_click)
    b1.place(x=20, y=250, width=40, height=40)
    # 2
    def b2_click():
        ent.insert(END, "2")
    b2 = Button(text="2", font="14", command=b2_click)
    b2.place(x=80, y=250, width=40, height=40)
    # 3
    def b3_click():
        ent.insert(END, "3")
    b3 = Button(text="3", font="14", command=b3_click)
    b3.place(x=140, y=250, width=40, height=40)
    # 4
    def b4_click():
        ent.insert(END, "4")
    b4 = Button(text="4", font="14", command=b4_click)
    b4.place(x=20, y=190, width=40, height=40)
    # 5
    def b5_click():
        ent.insert(END, "5")
    b5 = Button(text="5", font="14", command=b5_click)
    b5.place(x=80, y=190, width=40, height=40)
    # 6
    def b6_click():
        ent.insert(END, "6")
    b6 = Button(text="6", font="14", command=b6_click)
    b6.place(x=140, y=190, width=40, height=40)
    # 7
    def b7_click():
        ent.insert(END, "7")
    b7 = Button(text="7", font="14", command=b7_click)
    b7.place(x=20, y=130, width=40, height=40)
    # 8
    def b8_click():
        ent.insert(END, "8")
    b8 = Button(text="8", font="14", command=b8_click)
    b8.place(x=80, y=130, width=40, height=40)
    # 9
    def b9_click():
        ent.insert(END, "9")
    b9 = Button(text="9", font="14", command=b9_click)
    b9.place(x=140, y=130, width=40, height=40)

    # buttons +,-,/,*
    # .
    def point_click():
        ent.insert(END, ".")
    point = Button(text=".", font="14", command=point_click)
    point.place(x=140, y=310, width=40, height=40)
    # /
    def divide_click():
        global a,b 
        a = float(ent.get())
        b = "/"
        ent.delete(0, END)
    divide = Button(text="/", font="14", command=divide_click)
    divide.place(x=200, y=130, width=40, height=40)
    # *
    def multiply_click():
        global a,b 
        a = float(ent.get())
        b = "*"
        ent.delete(0, END)
    multiply = Button(text="*", font="14", command=multiply_click)
    multiply.place(x=200, y=190, width=40, height=40)
    # +
    def plus_click():
        global a,b 
        a = float(ent.get())
        b = "+"
        ent.delete(0, END)
    plus = Button(text="+", font="14", command=plus_click)
    plus.place(x=200, y=250, width=40, height=40)
    # -
    def minus_click():
        global a,b 
        a = float(ent.get())
        b = "-"
        ent.delete(0, END)
    minus = Button(text="-", font="14", command=minus_click)
    minus.place(x=200, y=310, width=40, height=40) 

    tk.mainloop()          
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
                launch_gui()
            elif choise == "6":
                print("Exit")
                break
            else:
                print("Invalid choice. Please try again.")
main()




