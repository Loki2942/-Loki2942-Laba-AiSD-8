import re
import random
from math import *
from itertools import count
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class TextWrapper:
    text_field: Text

    def __init__(self, text_field: Text):
        self.text_field = text_field

    def write(self, text: str):
        self.text_field.insert(END, text)

    def flush(self):
        self.text_field.update()

def combinations(lst, k):
    if k == 0:
        return [[]]
    res = []
    for i in range(len(lst)):
        elem = lst[i]
        rest = lst[i+1:]
        for j in combinations(rest, k-1):
            res.append([elem] + j)
    return res

def L(x1, y1, x2, y2): # для вычисления периметра треугольника
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def click_button():
    z = en_1.get()  # Записываем введенный текст в переменную "z"
    if not z.isdigit() or int(z)<3:
        messagebox.showinfo('Ошибка', "Вы ввели что-то не то, следуйте указаниям .")
    else:
        window = Tk()
        window.title("Результат")
        window.geometry("1000x500+150+20")
        text = ScrolledText(window,wrap=WORD)
        text.pack(fill=BOTH, side=TOP, expand=True)


        n = 25
        pairs = []
        for s in count(0, 1):
            if s >= int(z):
                break
            else:
                # генерируем два случайных числа и добавляем их в список в виде кортежа
                x = random.randint(0, n)
                y = random.randint(0, n)
                pairs.append((x, y))
        print(" \n Кординаты точек", pairs, file=TextWrapper(text))

        m = []
        for j in combinations(pairs, 3):  # составляем комбинаци  z по 3
            m.append(j)
        print('\nКоординаты точек возможных треугольников:', file=TextWrapper(text))

        max_perimeter = []
        for i in m:
            print(' Точка № 1: {}, Точка № 2: {}, Точка № 3: {}\n'.format(*i), file=TextWrapper(text))
            i = str(i)
            # ищем в списке i координаты
            x, y = list(map(list, zip(*[list(map(int, pair)) for pair in re.findall(r"\((\d+)\s*,\s*(\d+)\)", i)])))
            # перезапись для формулы
            x1, x2, x3 = x[0], x[1], x[2]
            y1, y2, y3 = y[0], y[1], y[2]
            # вычисляем периметр
            perimeter = round(L(x1, y1, x2, y2) + L(x2, y2, x3, y3) + L(x3, y3, x1, y1))
            max_perimeter.append(perimeter)
        # вывод
        print("Периметр самого большого треугольника: ", max(max_perimeter), "\n", file=TextWrapper(text))


root = Tk()  # создаем корневой объект - окно
root.title("л.р. №8")  # устанавливаем заголовок окна
root.geometry("1000x250+150+20")  # устанавливаем размеры окна
root.resizable(width=False, height=False)


Title = Label(text="Задание на л.р. №8:", font=("Times New Roman",16,"bold"))  # создаем текстовую метку
Title.pack(anchor="n")  # размещаем метку в окне
task = Label(text="Требуется для своего варианта второй\ части л.р. №6 (усложненной программы) или ее объектно-ориентированной"
                  " \nреализации (л.р. №7) разработать реализацию с использованием графического интерфейса." ,
             font=("Times New Roman",14),anchor="e").pack()


#блок для ввода\вывода информации
text1 = Label(text="\n\nВведите количество точек (число должно быть больше или равно 3)",font=("Times New Roman",14)).pack()
en_1 = Entry()  # создаем однострочное текстовое поле
en_1.pack()

btn = ttk.Button(text="Пуск", command=click_button).pack() #кнопка


root.mainloop()
