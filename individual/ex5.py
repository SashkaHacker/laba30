#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *


class RadioButtonInfo:
    def __init__(self, master, text, info, value):
        self.radiobutton = Radiobutton(
            master,
            text=text,
            indicatoron=0,
            variable=var,
            value=value,
            command=lambda i=info: self.show_info(i)
        )
        self.radiobutton.pack(anchor='w', side=LEFT, padx=5, pady=5)

    def show_info(self, info):
        label['text'] = info


if __name__ == "__main__":
    root = Tk()
    root.title("Информация о радиокнопках")

    var = IntVar()
    var.set(0)

    label = Label(root, text="Выберите радиокнопку", width=30)
    label.pack(pady=10)

    RadioButtonInfo(root, "Python", "Python - интерпретируемый язык программирования", 0)
    RadioButtonInfo(root, "Java", "Java - компилируемый язык программирования", 1)
    RadioButtonInfo(root, "C++", "C++ - компилируемый язык программирования", 2)

    root.mainloop()