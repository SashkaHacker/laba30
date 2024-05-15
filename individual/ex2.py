#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


# Функция, которая будет вызываться при нажатии на кнопку
def set_color(color_code, color_name):
    # Устанавливаем текст в текстовое поле и метку
    text_field.delete(0, tk.END)
    text_field.insert(0, color_code)
    label.config(text=color_name,)


# Создаем главное окно приложения
root = tk.Tk()
root.geometry("170x300")

root.title("Цвета радуги")

# Словарь с цветами и их кодами
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