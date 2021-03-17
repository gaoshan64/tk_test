from tkinter import *

from time_str import *

time_str = get_time_str()
print(time_str)


def p_time():
    time_str = time_input.get()
    who = who_input.get()

    print(time_str, who)


root = Tk()
root.title('Demo2')

time_label = Label(text='Time str')
time_label.grid(row=0, column=0)

who_lable = Label(text='更新人')
who_lable.grid(row=1, column=0)

time_input = Entry(textvariable=time_str)
time_input.insert(0, time_str)
time_input.grid(row=0, column=1)

who_input = Entry()
who_input.grid(row=1, column=1)

confirm_button = Button(text='Confirm', command=p_time)
confirm_button.grid(row=10, column=0, columnspan=2)

blank = Frame(width=5)
blank.grid(column=10)

root.mainloop()
