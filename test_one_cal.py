from tkinter import *

root = Tk()


def evalute(event):
    data = e.get()
    ans.configure(text='Answer:' + str(eval(data)))


tit = Label(root, text='请输入表达式')
tit.pack()

e = Entry(root)
e.bind("<Return>", evalute)
e.pack()

ans = Label(root)
ans.pack()

root.mainloop()
