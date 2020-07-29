from tkinter import *
import parser


root = Tk()
root.title("Calculator")

#funcion para obtener numeros y añadir numero hacia los lados
i = 0
def get_numbers(n):
    global i
    display.insert(i, n)
    i+=1 

def get_operation(operator):
    global i
    lenth_operator = len(operator)
    display.insert(i, operator)
    i+=lenth_operator

def clear():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear()
        display.insert(0, display_new_state)
    else:
        clear()   
        display.insert(0, "Error")   

def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear()
        display.insert(0, result)
    except:
        clear()
        display.insert(0, "Error math")

   

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)  #Crea un input

#Numeric Buttons 
Button(root, text="1", command=lambda:get_numbers(1)).grid(row=2, column=0, sticky=W+E) #Crea los botones numericos 
Button(root, text="2", command=lambda:get_numbers(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:get_numbers(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda:get_numbers(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:get_numbers(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:get_numbers(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda:get_numbers(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:get_numbers(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda:get_numbers(9)).grid(row=4, column=2, sticky=W+E)


#Buttons clear,0,%

Button(root, text="AC", command=lambda:clear()).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda:get_numbers(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=5, column=2, sticky=W+E)

#Buttons operations

Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3, sticky=W+E)

Button(root, text="←", command=lambda: undo()).grid(row=2, column=4, sticky=W+E, columnspan = 2)
Button(root, text="exp",command=lambda: get_operation("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2",command=lambda: get_operation("*2")).grid(row=3, column=5, sticky=W+E)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=4, sticky=W+E)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=4, sticky=W+E, columnspan = 2)




root.mainloop()
    

    