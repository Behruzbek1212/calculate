from tkinter import*

oyna = Tk()
oyna.geometry('265x200')
oyna.title('Kalkulyator')
oyna.configure(background = 'lightgreen')

expression = ''

result = StringVar()
ex = Entry(textvariable=result)
ex.grid(columnspan=4, ipadx=70)

def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression = total
    except:
        result.sot('error')
        
        expression = ''

def reset():
    global expression
    total = ''
    result.set(total)
    expression = total
        

    

button1 = Button(text = '1', height=1, width=7, command=lambda: press_num(1))
button1.grid(row=2, column=0)

button2 = Button(text = '2', height=1, width=7, command=lambda: press_num(2))
button2.grid(row=2, column=1)

button3 = Button(text = '3', height=1, width=7, command=lambda: press_num(3))
button3.grid(row=2, column=2)

button4 = Button(text = '4', height=1, width=7, command=lambda: press_num(4))
button4.grid(row=3, column=0)

button5 = Button(text = '5', height=1, width=7, command=lambda: press_num(5))
button5.grid(row=3, column=1)

button6 = Button(text = '6', height=1, width=7, command=lambda: press_num(6))
button6.grid(row=3, column=2)

button7 = Button(text = '7', height=1, width=7, command=lambda: press_num(7))
button7.grid(row=4, column=0)

button8 = Button(text = '8', height=1, width=7, command=lambda: press_num(8))
button8.grid(row=4, column=1)

button9 = Button(text = '9', height=1, width=7, command=lambda: press_num(9))
button9.grid(row=4, column=2)

button0 = Button(text = '0', height=1, width=7, command=lambda: press_num(0))
button0.grid(row=5, column=1)

plus = Button(text = '+', height=1, width=7, command=lambda: press_num('+'))
plus.grid(row=5, column=0)

button0 = Button(text = '-', height=1, width=7, command=lambda: press_num('-'))
button0.grid(row=6, column=0)

plus = Button(text = '*', height=1, width=7, command=lambda: press_num('*'))
plus.grid(row=5, column=2)

button0 = Button(text = '/', height=1, width=7, command=lambda: press_num('/'))
button0.grid(row=6, column=2)

equal = Button(text = '=', height=1, width=7, command=equalpress)
equal.grid(row=6, column=1)

reset = Button(text = 'RESET', height=1, width=7, command=reset)
reset.grid(row=8, column=1)



oyna.mainloop()