#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите программу, состоящую из однострочного и многострочного
# текстовых полей и двух кнопок "Открыть" и "Сохранить". При клике на первую должен
# открываться на чтение файл, чье имя указано в поле класса Entry , а содержимое файла
# должно загружаться в поле типа Text .
# При клике на вторую кнопку текст, введенный пользователем в экземпляр Text , должен
# сохраняться в файле под именем, которое пользователь указал в однострочном текстовом
# поле.
# Файлы будут читаться и записываться в том же каталоге, что и файл скрипта, если указывать
# имена файлов без адреса

import tkinter as tk
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(defaultextension=".txt")
    if filename:
        try:
            with open(filename, "r") as file:
                text = file.read()
            text_editor.delete("1.0", tk.END)
            text_editor.insert("1.0", text)
            entry_filename.delete(0, tk.END)
            entry_filename.insert(0, filename)
        except FileNotFoundError:
            tk.messagebox.showerror("Ошибка", f"Файл не найден: {filename}")


def save_file():
    filename = entry_filename.get()
    if filename:
        try:
            with open(filename, "w") as file:
                text = text_editor.get("1.0", tk.END)
                file.write(text)
        except FileNotFoundError:
            tk.messagebox.showerror("Ошибка", f"Файл не найден: {filename}")


if __name__ == "__main__":
    master = tk.Tk()
    master.title("Редактор файлов")

    entry_filename = tk.Entry(master, width=30)
    text_editor = tk.Text(master)
    button_open = tk.Button(
        master, text="Открыть", command=open_file
    )
    button_save = tk.Button(
        master, text="Сохранить", command=save_file
    )
    entry_filename.grid(row=0, column=0)
    button_open.grid(row=0, column=1)
    button_save.grid(row=0, column=2)
    text_editor.grid(row=1, column=0, columnspan=3)
    master.mainloop()
