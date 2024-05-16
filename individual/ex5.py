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


def show_info(compiled):
    if compiled:
        label['text'] = "компилируемый ЯП"
    else:
        label['text'] = "некомпилируемый ЯП"


if __name__ == "__main__":
    root = Tk()
    root.title("Информация о радиокнопках")

    var = IntVar()
    var.set(0)

    label = Label(root, text="Выберите радиокнопку", width=20, height=2)
    label.pack(pady=10)

    radio_buttons_info = [
        ("Python", False, 0),
        ("Java", True, 1),
        ("C++", True, 2)
    ]

    radio_frame = Frame(root)
    radio_frame.pack(side=LEFT, fill=Y, padx=5, pady=5)

    for text, is_compiled, value in radio_buttons_info:
        rb = Radiobutton(
            radio_frame,
            text=text,
            indicatoron=0,
            variable=var,
            value=value,
            command=lambda compiled=is_compiled: show_info(compiled),
            width=20,
            height=2
        )
        rb.pack(anchor='w', padx=5, pady=5)

    root.mainloop()