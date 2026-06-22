''' Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной сумму этих значений,
# а если равны, то присвоить переменным нулевые значения. Вывести новые значения переменных A и B.'''

import tkinter as tk
from tkinter import messagebox



def calculate():
    try:

        A = int(entry_A.get())
        B = int(entry_B.get())


        if A != B:
            сумма = A + B
            A = сумма
            B = сумма
        else:
            A = 0
            B = 0


        label_result.config(text=f"Новые значения:\nA = {A}, B = {B}")

    except ValueError:

        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа!")


'''okno'''
root = tk.Tk()
root.title("Решение задачи")
root.geometry("300x250")



'''pole a'''
label_A = tk.Label(root, text="Введите число для А:")
label_A.pack(pady=5)
entry_A = tk.Entry(root)
entry_A.pack(pady=5)

'''pole b'''
label_B = tk.Label(root, text="Введите число для В:")
label_B.pack(pady=5)
entry_B = tk.Entry(root)
entry_B.pack(pady=5)

'''vichislenie'''
btn_calc = tk.Button(root, text="Вычислить", command=calculate)
btn_calc.pack(pady=10)


label_result = tk.Label(root, text="Результат появится здесь", fg="blue")
label_result.pack(pady=5)


root.mainloop()