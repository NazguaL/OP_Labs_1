from tkinter import *

root = Tk()
root.title("AboutForm")
root.geometry("400x300")

'''
text_h1 = Text(width=50, height=2)
text_h1.pack()
text_h1.insert(1.0, "Hello world!")
text_h1.tag_add('title', 1.0, '1.end')
text_h1.tag_config('title', font=("Verdana", 24, 'bold'), justify=CENTER)
'''
lbl1 = Label(root, text="", bg="orange red", fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()

label_h1 = Label(root, text="Лабораторная работа №1")
label_h1.config(font=("Verdana", 18, 'bold'), anchor=CENTER)
label_h1.pack()


def close_window():
    root.destroy()

button = Button(text="Выход", command=close_window).place(x=300, y=250, width=60)

root.mainloop()



