from tkinter import *
from tkinter import ttk
import re
import random
from math import *
from contextlib import redirect_stdout


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

# для вычисления периметра треугольника
def L(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

def is_valid(newval):
    result=  re.match("[3-9]\d*", newval) is not None
    if not result :
        errmsg.set("Вы ввели что-то не то, следуйте указаниям .")
    else:
        errmsg.set("")
    return result

def click_button():
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x500")
    text = Text(window)
    text.pack()

    z = en_1.get()  # Записываем введенный текст в переменную "а"
    print(z)
    n = 25
    pairs = []
    s = 0  # индикатор заполнения
    while s != z:
        # генерируем два случайных числа и добавляем их в список в виде кортежа
        x = random.randint(0, n)
        y = random.randint(0, n)
        # ограничение на характеристики объектов
        if (x + y) % 3 == 0:
            if not (x, y) in pairs:  # защита от одинаковых точек
                pairs.append((x, y))
                s += 1
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
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("1000x600+150+20")  # устанавливаем размеры окна
root.minsize(200,150)   # минимальные размеры: ширина - 200, высота - 150
root.maxsize(1100,700)   # максимальные размеры: ширина - 1100, высота - 700



Title = Label(text="Задание на л.р. №8:", font=("Times New Roman",14,"bold"))  # создаем текстовую метку
Title.pack(anchor="n")  # размещаем метку в окне
task = Label(text="Требуется для своего варианта второй\ части л.р. №6 (усложненной программы) или ее объектно-ориентированной"
                  " \nреализации (л.р. №7) разработать реализацию с использованием графического интерфейса.\n"
                  "\nЗадание на л.р. №6:\n"
                  "Вариант 16. На плоскости задано К точек. Сформировать все возможные варианты выбора множества точек из них\n"
                  "для формирования всех возможных треугольников. В усложненной программе необходимо чтобы сумма координат\n "
                  "точки была кратна трём,"
                  "затем рассчитать периметр треугольника по координатам,периметр самого большого \nтреугольника, вывести в консоль.",
             font=("Times New Roman",12),anchor="e").pack()



#блок для ввода\вывода информации
text1 = Label(text="\n\nВведите количество точек (число должно быть больше или равно 3)").pack()


check = (root.register(is_valid), "%P")
errmsg = StringVar()
en_1 = Entry(validate="key", validatecommand=check)  # создаем однострочное текстовое поле
en_1.pack()
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack()
btn = ttk.Button(text="Пуск", command=click_button).pack() #кнопка


root.protocol("WM_DELETE_WINDOW", finish)
root.mainloop()