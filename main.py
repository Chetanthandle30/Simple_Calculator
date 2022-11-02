# Building a Simple Calculator

import tkinter as tk

calculation = ''


# Input for variable
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


# Defining a solution
def solution():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)
    except:
        clear()
        text_result.insert(1.0, 'Error')


# Define a function to clear the previous expressions
def clear():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')


# Define to clear the last element of the expression
def delete():
    global calculation

    if calculation == '':
        text_result.insert(1.0, '0')

    else:
        calculation = calculation.rstrip(calculation[-1])
        new = calculation
        clear()
        calculation = new
        text_result.insert(1.0, calculation)


# Initialise the table for the program
root = tk.Tk()
root.geometry('300x275')  # Define the geometry
root.title('Simple Calculator')  # Title for the calculator

text_result = tk.Text(root, height=1, width=16, font=('Arial', 24))
text_result.grid(columnspan=5)

# Initialise the operation and numbers
button1 = tk.Button(root, text='1', command=lambda: add_to_calculation(1), width=5, font=('Arial', 14))
button1.grid(row=2, column=1)

button2 = tk.Button(root, text='2', command=lambda: add_to_calculation(2), width=5, font=('Arial', 14))
button2.grid(row=2, column=2)

button3 = tk.Button(root, text='3', command=lambda: add_to_calculation(3), width=5, font=('Arial', 14))
button3.grid(row=2, column=3)

button4 = tk.Button(root, text='4', command=lambda: add_to_calculation(4), width=5, font=('Arial', 14))
button4.grid(row=3, column=1)

button5 = tk.Button(root, text='5', command=lambda: add_to_calculation(5), width=5, font=('Arial', 14))
button5.grid(row=3, column=2)

button6 = tk.Button(root, text='6', command=lambda: add_to_calculation(6), width=5, font=('Arial', 14))
button6.grid(row=3, column=3)

button7 = tk.Button(root, text='7', command=lambda: add_to_calculation(7), width=5, font=('Arial', 14))
button7.grid(row=4, column=1)

button8 = tk.Button(root, text='8', command=lambda: add_to_calculation(8), width=5, font=('Arial', 14))
button8.grid(row=4, column=2)

button9 = tk.Button(root, text='9', command=lambda: add_to_calculation(9), width=5, font=('Arial', 14))
button9.grid(row=4, column=3)

button0 = tk.Button(root, text='0', command=lambda: add_to_calculation(0), width=5, font=('Arial', 14))
button0.grid(row=5, column=2)

button_add = tk.Button(root, text='+', command=lambda: add_to_calculation('+'), width=5, font=('Arial', 14))
button_add.grid(row=2, column=4)

button_subtract = tk.Button(root, text='-', command=lambda: add_to_calculation('-'), width=5, font=('Arial', 14))
button_subtract.grid(row=3, column=4)

button_multiply = tk.Button(root, text='*', command=lambda: add_to_calculation('*'), width=5, font=('Arial', 14))
button_multiply.grid(row=4, column=4)

button_divide = tk.Button(root, text='/', command=lambda: add_to_calculation('/'), width=5, font=('Arial', 14))
button_divide.grid(row=5, column=4)

button_open_parenthesis = tk.Button(root, text='(', command=lambda: add_to_calculation('('), width=5,
                                    font=('Arial', 14))
button_open_parenthesis.grid(row=5, column=1)

button_close_parenthesis = tk.Button(root, text=')', command=lambda: add_to_calculation(')'), width=5,
                                     font=('Arial', 14))
button_close_parenthesis.grid(row=5, column=3)

button_equals = tk.Button(root, text='=', command=solution, width=10, font=('Arial', 14))
button_equals.grid(row=6, column=3, columnspan=2)

button_clear = tk.Button(root, text='c', command=clear, width=5, font=('Arial', 14))
button_clear.grid(row=6, column=1)

button_delete = tk.Button(root, text='del', command=delete, width=5, font=('Arial', 14))
button_delete.grid(row=6, column=2)

root.mainloop()
