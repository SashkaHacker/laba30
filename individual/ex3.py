#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: перепишите программу из пункта 8 так, чтобы интерфейс выглядел
# примерно следующим образом:

import tkinter as tk


def set_color(color_code, color_name):
    text_field.delete(0, tk.END)
    text_field.insert(0, color_code)
    label.config(text=color_name, )


if __name__ == "__main__":
    root = tk.Tk()

    root.title("Цвета радуги")

    colors = {
        "Красный": "#ff0000",
        "Оранжевый": "#ff7d00",
        "Желтый": "#ffff00",
        "Зеленый": "#00ff00",
        "Голубой": "#007dff",
        "Синий": "#0000ff",
        "Фиолетовый": "#7d00ff"
    }

    text_field = tk.Entry(root, width=20)
    text_field.pack()
    label = tk.Label(root, text="", font=("Arial", 14))
    label.pack()

    for color_name, color_code in colors.items():
        button = tk.Button(root, bg=color_code,
                           command=lambda c=color_code,
                                          n=color_name: set_color(c, n),
                           height=2, width=4)
        button.pack(side=tk.LEFT)

    root.mainloop()
