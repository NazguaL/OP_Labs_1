from tkinter import *

root = Tk()
root.title("AboutForm")
root.geometry("400x300")

label_h1 = Label(root, text="Лабораторна робота №1")
label_h1.config(font=("Verdana", 16, 'bold'), justify=CENTER, pady=15)
label_h1.pack()

label_group_number = Label(root, text="Виконав студент групи ЗПІ 91")
label_group_number.config(font=("Verdana", 10), justify=CENTER, pady=10)
label_group_number.pack()

label_name = Label(root, text="Івашко Сергій Володимирович")
label_name.config(font=("Verdana", 16), justify=CENTER, pady=10)
label_name.pack()


def close_window():
    root.destroy()

button = Button(text="Вихід", command=close_window).place(x=300, y=250, width=60)

root.mainloop()



