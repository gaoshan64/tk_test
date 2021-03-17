from tkinter import *
from tkinter.ttk import *

from time_str import *

time_str = get_time_str()
print(time_str)


def change_workshop_value(event):
    if dep_dropbox.get() == 'SF':
        workshop_dropbox['value'] = ['ZA', 'ZB', 'ZP']
    elif dep_dropbox.get() == 'TC':
        workshop_dropbox['value'] = ['PREP', 'ASSM1', 'ASSM2', 'APCU']
    elif dep_dropbox.get() == 'PL':
        workshop_dropbox['value'] = ['PREP', 'ASSM', 'APCU']
    elif dep_dropbox.get() == 'SITE':
        workshop_dropbox['value'] = ['MIS', 'NF', 'NCM', 'OFFICE']
    else:
        workshop_dropbox['value'] = ['ZA', 'ZB', 'ZP', 'PREP', 'ASSM', 'ASSM1', 'ASSM2', 'APCU', 'MIS', 'NF', 'NCM',
                                     'OFFICE']


def p_time():
    time_str = time_input.get()
    who = who_input.get()
    dep = dep_dropbox.get()
    workshop = workshop_dropbox.get()
    print(time_str, who, dep, workshop)


root = Tk()
root.title('Demo2')

dep_lable = Label(text='部门')
dep_lable.grid(row=5, column=0)

dep_dropbox = Combobox()
dep_dropbox['value'] = ['SF', 'TC', 'PL', 'SITE']
dep_dropbox.bind('<<ComboboxSelected>>', change_workshop_value)
dep_dropbox.grid(row=5, column=10)

workshop_lable = Label(text='车间')
workshop_lable.grid(row=6, column=0)

workshop_dropbox = Combobox()
workshop_dropbox['value'] = ['ZA', 'ZB', 'ZP', 'PREP', 'ASSM', 'ASSM1', 'ASSM2', 'APCU', 'MIS', 'NF', 'NCM', 'OFFICE']
workshop_dropbox.grid(row=6, column=10)

time_label = Label(text='Time str')
time_label.grid(row=9, column=0)

who_lable = Label(text='更新人')
who_lable.grid(row=10, column=0)

time_input = Entry(textvariable=time_str)
time_input.insert(0, time_str)
time_input.grid(row=9, column=10)

who_input = Entry()
who_input.grid(row=10, column=10)

confirm_button = Button(text='Confirm', command=p_time)
confirm_button.grid(row=100, column=0, columnspan=11)

blank = Frame(width=5)
blank.grid(column=100)

root.mainloop()
