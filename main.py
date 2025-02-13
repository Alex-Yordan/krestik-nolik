import tkinter as tk
from tkinter import messagebox

window = tk.Tk() #Создание окна приложения
window.title("Крестики-нолики") #Заголовок окна
window.geometry("300x350") #Размеры окна

current_player = "X" #Переменная для игрока Х
buttons = [] #Список для хранения всех 9-ти кнопок

# Логика игры
def on_click(row, col): # Функция, определяющая место клика
    pass

for i in range(3): #Цикл для создания строк поля
    row = [] #Список для добавления кнопок текущей строки
    for j in range(3): #Цикл для создания кнопок внутри строки
        #Переменная btn для создания кнопки с аргументами (текст, шрифт, ширина)
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j) #Метод определяющий конкретное место для каждой кнопки
        row.append(btn) #Добавление кнопки внутри ряда
    buttons.append(row) #Добавление сразу 3 кнопок в список buttons

window.mainloop() # Чтобы окно не закрывалось
