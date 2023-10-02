import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring


def button_click(i, j):
    if board[i][j] == " ":
        board[i][j] = current_player
        buttons[i][j].config(text=current_player)


root = tk.Tk()
board = [[" " for x in range(3)] for x in range(3)]
buttons = []
for x in range(3):
    row_buttons = []
    for y in range(3):
        button = tk.Button(root,text=" ", height=4, width=10, command=lambda row=x, col=y: button_click(row,col))
        button.grid(row=x,column=y)
        row_buttons.append(button)
    buttons.append(row_buttons)

current_player = askstring("Начало", "Введите Х или 0")
if current_player == "X" or current_player == "0":
    print(f"Игрок выбрал {current_player}")
    root.mainloop()
elif current_player:
    messagebox.showerror("Ошибка","Пожалуйста, выберите Х или 0")
else:
    messagebox.showerror("Ошибка", "Пользователь отменил ввод")

