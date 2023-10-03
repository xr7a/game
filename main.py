import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring


def player_pick():
    global current_player
    current_player = askstring("Начало", "Введите Х или 0")
    if current_player == "X" or current_player == "0":
        print(f"Игрок выбрал {current_player}")
        root.mainloop()
    elif current_player:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите Х или 0")
        restart()
    else:
        messagebox.showerror("Ошибка", "Пользователь отменил ввод")
        root.destroy()


def button_click(i, j):
    global current_player
    if board[i][j] == "X" or board[i][j] == "0":
        messagebox.showerror('Ошибка', 'Поле занято')
        return 0
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
current_player = " "
player_pick()
