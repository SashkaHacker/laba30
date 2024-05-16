#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите простейший калькулятор, состоящий из двух текстовых полей,
# куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". Результат вычисления
# должен отображаться в метке. Если арифметическое действие выполнить невозможно
# (например, если были введены буквы, а не числа), то в метке должно появляться слово
# "ошибка".

import tkinter as tk


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2

        label.config(text=f"Результат: {result}")
    except ValueError:
        label.config(text="Ошибка")
    except ZeroDivisionError:
        label.config(text="Ошибка: деление на ноль")


if __name__ == "__main__":
    master = tk.Tk()
    master.title("Калькулятор")

    entry1 = tk.Entry(master, width=10)
    entry2 = tk.Entry(master, width=10)
    label = tk.Label(master, text="Результат:")

    button_add = tk.Button(master, text="+", command=lambda: calculate('+'))
    button_sub = tk.Button(master, text="-", command=lambda: calculate('-'))
    button_mul = tk.Button(master, text="*", command=lambda: calculate('*'))
    button_div = tk.Button(master, text="/", command=lambda: calculate('/'))

    entry1.grid(row=0, column=0)
    entry2.grid(row=0, column=1)
    label.grid(row=1, column=0, columnspan=2)
    button_add.grid(row=2, column=0)
    button_sub.grid(row=2, column=1)
    button_mul.grid(row=3, column=0)
    button_div.grid(row=3, column=1)

    master.mainloop()