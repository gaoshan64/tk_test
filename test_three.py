from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Demo3')

time_label = Label(text='Time str')
time_label.grid(row=0, column=0)
who_lable = Label(text='更新人')
who_lable.grid(row=1, column=0)

f1 = Frame(width=5)
f2 = Frame(width=5)
f1.grid(row=0, column=3)
time_input = Entry()
time_input.grid(row=0, column=1)
who_input = Entry()
who_input.grid(row=1, column=1)

confirm_button = Button(text='Confirm')
confirm_button.grid(row=30, column=0, columnspan=2)

root.mainloop()
