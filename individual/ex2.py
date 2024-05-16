#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите программу, состоящую из семи кнопок, цвета которых
# соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
# вставляться код цвета, а в метку – название цвета.
# Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый,
# #ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff –
# фиолетовый.

import tkinter as tk


def set_color(color_code, color_name):
    text_field.delete(0, tk.END)
    text_field.insert(0, color_code)
    label.config(text=color_name,)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("170x300")
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

    # Текстовое поле для отображения кода цвета
    text_field = tk.Entry(root, width=20)
    text_field.pack()

    # Метка для отображения названия цвета
    label = tk.Label(root, text="", font=("Arial", 14))
    label.pack()

    # Создаем кнопки для каждого цвета
    for color_name, color_code in colors.items():
        button = tk.Button(root, bg=color_code,
                           command=lambda c=color_code, n=color_name: set_color(c, n))
        button.pack(fill=tk.X)

    root.mainloop()
