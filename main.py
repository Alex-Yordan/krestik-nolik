import tkinter as tk
from tkinter import messagebox

window = tk.Tk() # Создание окна приложения
window.title("Крестики-нолики") # Заголовок окна
window.geometry("275x275") # Размеры окна

current_player = "X" # Переменная для игрока
buttons = [] # Список для хранения всех 9-ти кнопок

# Логика игры
def check_winner(): # Функция проверки на победителя
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "": # Проверка ряда на одинаковость знаков
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "": # Проверка столбца на одинаковость знаков
            return True
        if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "": # Проверка диагонали на одинаковость знаков
            return True
        if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "": # Проверка диагонали на одинаковость знаков
            return True

    return False

def on_click(row, col): # Функция, определяющая место клика
    global current_player # Переменная, которая следит чей ход Х или 0

    if buttons[row][col]['text'] == "":  # Проверка, что клетка пустая
        buttons[row][col]['text'] = current_player # Присваиваем текст кнопке, соответствующий игроку

    if check_winner(): # Проверяет, есть ли победитель и выводит сообщение
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        
    current_player = "0" if current_player == "X" else "X" # Переключение игроков

for i in range(3): # Цикл для создания строк поля
    row = [] # Список для добавления кнопок текущей строки
    for j in range(3): # Цикл для создания кнопок внутри строки
        # Переменная btn для создания кнопки с аргументами (текст, шрифт, ширина)
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j) # Метод определяющий конкретное место для каждой кнопки
        row.append(btn) # Добавление кнопки внутри ряда
    buttons.append(row) # Добавление сразу 3 кнопок в список buttons

window.mainloop() # Чтобы окно не закрывалось
