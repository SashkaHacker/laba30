#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Решите задачу: виджеты Radiobatton и Checkbutton поддерживают большинство свойств
# оформления внешнего вида, которые есть у других элементов графического интерфейса.
# При этом у Radiobutton есть особое свойство indicatoron . По-умолчанию он равен
# единице, в этом случае радиокнопка выглядит как нормальная радиокнопка. Однако если
# присвоить этой опции ноль, то виджет Radiobutton становится похожим на обычную кнопку
# по внешнему виду. Но не по смыслу.
# Напишите программу, в которой имеется несколько объединенных в группу радиокнопок,
# индикатор которых выключен ( indicatoron=0 ). Если какая-нибудь кнопка включается, то в
# метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть
# не должно

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