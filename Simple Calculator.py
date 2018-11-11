# Calculator created using Tkinter
# Simple python program that uses GUI

# import tkinter module
from tkinter import *

# declare expression blank
expression = ""

# Function that updates expression in the text entry box
def press(num):
    # create global variable
    global expression

    # concatenate string
    expression = expression + str(num)

    # update expression
    equation.set(expression)

# Function that calculates final expression
def equalpress():
    # Try and catch

    try:

        global expression

        # evaluate function to evaluate the expression
        # and str function to convert the result into a string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable

    except:

        equation.set(" ERROR ")
        expression = "" # reset the expression

# Function to clear contents
def clear():
    global expression
    expression = "" # reset the expression
    equation.set("")

# Driver code displays GUI
if __name__ == "__main__":
    # this creates a GUI
    gui = Tk() # call unto Tkinter

    # set background colour
    gui.configure(background= "white")

    # set title of GUI
    gui.title("Calculator")

    # set the configuration of GUI window
    gui.geometry("265x125")

    # StringVar() variable class
    # Create instance of class
    equation = StringVar()

    # Create text entry box for showing user entered expression
    expression_field = Entry(gui, textvariable=equation)

    # Using grid method for placing widgets
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set("Enter your expression")

    # create buttons and place particular location inside the original window
    button1 = Button(gui, text= "1", fg= "black", bg = "SteelBlue", command= lambda: \
                     press(1), height = 1, width = 7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text= "2", fg="black", bg = "SteelBlue", command= lambda: \
                     press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text = "3", fg = "black", bg = "SteelBlue", command = lambda: \
                     press(3), height = 1, width = 7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text= "4", fg ="black", bg = "SteelBlue", command = lambda: \
                     press(4), height= 1, width = 7)
    button4.grid(row=3, column=0)
    
    button5 = Button(gui, text= "5", fg ="black", bg = "SteelBlue", command = lambda: \
                     press(5), height= 1, width = 7)
    button5.grid(row=3, column=1)
    
    button6 = Button(gui, text= "6", fg ="black", bg = "SteelBlue", command = lambda: \
                     press(6), height= 1, width = 7)
    button6.grid(row=3, column=2)
    
    button7 = Button(gui, text= "7", fg ="black", bg = "SteelBlue", command = lambda: \
                     press(7), height= 1, width = 7)
    button7.grid(row=4, column=0)
    
    button8 = Button(gui, text= "8", fg ="black", bg = "SteelBlue", command = lambda: \
                     press(8), height= 1, width = 7)
    button8.grid(row=4, column=1)
    
    button9 = Button(gui, text= "9", fg ="black", bg = "SteelBlue", command = lambda: \
                     press(9), height= 1, width = 7)
    button9.grid(row=4, column=2)

    button0 = Button(gui,text = "0", fg = "black", bg = "SteelBlue", command = lambda: \
                     press(0), height = 1, width = 7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text= "+", fg = "black", bg = "gray", command = lambda: \
                  press("+"), height = 1, width = 7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text = "-", fg = "black", bg = "gray", command = lambda: \
                   press("-"), height = 1, width = 7)
    minus.grid(row=3, column = 3)

    multiply = Button(gui,text=" * ", fg = "black", bg = "gray", command = lambda: \
                      press("*"), height=1, width= 7)
    multiply.grid(row=4, column = 3)

    divide = Button(gui, text= " / ", fg = "black", bg = "gray", command = lambda: \
                    press("/"), height=1, width = 7)
    divide.grid(row=5, column = 3)

    equal = Button(gui, text=" = ", fg = "black", bg = "gray", command = equalpress, \
                height =1, width = 7)
    equal.grid(row=5, column = 2)

    clear = Button(gui, text="Clear", fg="black", bg="gray", command=clear, height=1, \
                   width = 7)
    clear.grid(row=5, column = 1)

    #startup the GUI
    gui.mainloop()
    

    
    

                     
        

                    
    
    

    

    
        
    

