#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


class InfoButtons:
    def __init__(self, master):
        self.master = master
        master.title("Информация")

        self.info = {
            "Кнопка 1": "Информация для кнопки 1",
            "Кнопка 2": "Информация для кнопки 2",
            "Кнопка 3": "Информация для кнопки 3"
        }

        self.var = tk.StringVar(value="Кнопка 1")
        self.label = tk.Label(master, text=self.info["Кнопка 1"])

        row = 0
        for name in self.info.keys():
            button = tk.Radiobutton(master, text=name, variable=self.var, value=name, indicatoron=0, command=self.show_info)
            button.grid(row=row, column=0)
            row += 1

        self.label.grid(row=row, column=0)

    def show_info(self):
        selected_button = self.var.get()
        self.label.config(text=self.info[selected_button])


if __name__ == "__main__":
    root = tk.Tk()
    info_buttons = InfoButtons(root)
    root.mainloop()