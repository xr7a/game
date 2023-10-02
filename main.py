import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring

def checkWinner(board):
    for row in board:
        if all(x == current_player for x in row):
            return True
        if all(board[i][j] == current_player for i in range(3) for j in range(3)):
            return True
        if all(board[i][i] == current_player for i in range(3)) or all(board[i][2-i] == current_player for i in range(3)):
            return True
    return False


def button_click(i, j):
        global current_player
        if board[i][j] == " ":
            board[i][j] = current_player
            buttons[i][j].config(text=current_player)
        if checkWinner(board):
            messagebox.showinfo("Победа", f"Победил игрок {current_player}!!")
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            messagebox.showinfo("НИЧЬЯ","Победила дружба!!")
        else:
            current_player = "0" if current_player == "X" else "X"



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
