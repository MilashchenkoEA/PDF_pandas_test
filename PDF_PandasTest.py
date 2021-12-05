__author__ = 'MilaschenkoEA'

import random
import math
import matplotlib.pyplot as plt
import pandas as pd


def rel_rand(n: int, rel_sigma: float):
    """Генерирует случайные числа
    с Релеевской плотностью распределения вероятности, где
    n - количество отсчетов,
    rel_sigma - среднеквадратическое отклонение"""
    rel_list = []
    for i in range(n):
        rel_list.append((rel_sigma / math.sqrt(2)) * math.sqrt(-2 * math.log(random.uniform(0, 1))))
    return rel_list


def rel_pdf(rel_sigma: float, n: int, delta_x: float):
    pdf_x = []
    pdf_y = []
    for i in range(1, n):
        x = i * delta_x
        pdf_x.append(x)
        pdf_y.append(((2 * x) / rel_sigma) * math.exp((-x ** 2) / rel_sigma))
    return pd.DataFrame({'x': pdf_x, 'y': pdf_y})


def gam_rand(n: int, v: float, b: float):
    gam_list = []
    for i in range(n):
        gam_list.append(random.gammavariate(v, 1 / b))
    return gam_list


def gam_pdf(v: float, b: float, n: int, delta_x: float):
    pdf_x = []
    pdf_y = []
    for i in range(1, n):
        x = i * delta_x
        pdf_x.append(x)
        pdf_y.append(((b ** v) / math.gamma(v) * (x ** (v - 1)) * math.exp(-b * x)))
    return pd.DataFrame({'x': pdf_x, 'y': pdf_y})


def weib_rand(n: int, a: float, b: float):
    wei_list = []
    for i in range(n):
        wei_list.append(random.weibullvariate(a, b))
    return wei_list


def weib_pdf(a: float, b: float, n: int, delta_x: float):
    pdf_x = []
    pdf_y = []
    for i in range(1, n):
        x = i * delta_x
        pdf_x.append(x)
        pdf_y.append((b / a) * ((x / a) ** (b - 1)) * math.exp(-(x / a) ** b))
    return pd.DataFrame({'x': pdf_x, 'y': pdf_y})


def exp_rand(n: int, l: float):
    exp_list = []
    for i in range(n):
        exp_list.append(random.expovariate(l))
    return exp_list


def exp_pdf(l: float, n: int, delta_x: float):
    pdf_x = []
    pdf_y = []
    for i in range(1, n):
        x = i * delta_x
        pdf_x.append(x)
        pdf_y.append(l * math.exp(-l * x))
    return pd.DataFrame({'x': pdf_x, 'y': pdf_y})


rrand = rel_rand(100000, 1)
rel = rel_pdf(1, 100, 0.05)

grand = gam_rand(100000, 0.5, 0.5)
gam = gam_pdf(0.5, 0.5, 500, 0.01)

wrand = weib_rand(100000, 1, 5)
weib = weib_pdf(1, 5, 500, 0.01)

exprand = exp_rand(100000, 1.5)
exp = exp_pdf(1.5, 500, 0.01)

# Построение графиков
fig, ax = plt.subplots(nrows=2, ncols=2)  # Создаем фигуру и четыре системы координат на фигуре

ax[0, 0].plot(rel['x'], rel['y'], 'b-', label='PDF')  # Плотность распределения построенная по формуле
pd_s = pd.Series(rrand)
pd_s.plot(kind='kde', color='green', legend='true', label='PandasPDF', ax=ax[0, 0])  # Плотность распределения
# построенная средствами Pandas
ax[0, 0].set(title='Релеевское распределение')  # Заголовок для системы координат
ax[0, 0].set_xlabel('x')  # Ось абсцисс
ax[0, 0].set_ylabel('PDF(x)')  # Ось ординат
ax[0, 0].set_xlim(xmin=0, xmax=4)  # Минимальное и максимальное значение по оси Х
ax[0, 0].legend()  # Отображаем легенду для данной системы координат
ax[0, 0].grid()  # Отображаем сетку на системе координат

ax[0, 1].plot(gam['x'], gam['y'], 'b-', label='PDF')  # Плотность распределения построенная по формуле
pd_s = pd.Series(grand)
pd_s.plot(kind='kde', color='green', legend='true', label='PandasPDF', ax=ax[0, 1])  # Плотность распределения
# построенная средствами Pandas
ax[0, 1].set(title='Гамма распределение')  # Заголовок для системы координат
ax[0, 1].set_xlabel('x')  # Подписи по оси абсцисс
ax[0, 1].set_ylabel('PDF(x)')  # Подписи по оси ординат
ax[0, 1].set_xlim(xmin=0, xmax=4)  # Минимальное и максимальное значение по оси Х
ax[0, 1].legend()  # Отображаем легенду для данной системы координат
ax[0, 1].grid()  # включение отображение сетки

ax[1, 0].plot(weib['x'], weib['y'], 'b-', label='PDF')  # Плотность распределения построенная по формуле
pd_s = pd.Series(wrand)
pd_s.plot(kind='kde', color='green', legend='true', label='PandasPDF', ax=ax[1, 0])  # Плотность распределения
# построенная средствами Pandas
ax[1, 0].set(title='Распределение Вейбулла')
ax[1, 0].set_xlabel('x')  # ось абсцисс
ax[1, 0].set_ylabel('PDF(x)')  # ось ординат
ax[1, 0].set_xlim(xmin=0, xmax=4)
ax[1, 0].legend()
ax[1, 0].grid()  # включение отображение сетки

ax[1, 1].plot(exp['x'], exp['y'], 'b-', label='PDF')  # Плотность распределения построенная по формуле
pd_s = pd.Series(exprand)
pd_s.plot(kind='kde', color='green', legend='true', label='PandasPDF', ax=ax[1, 1])  # Плотность распределения
# построенная средствами Pandas
ax[1, 1].set(title='Экспоненциальное распределение')
ax[1, 1].set_xlabel('x')  # ось абсцисс
ax[1, 1].set_ylabel('PDF(x)')  # ось ординат
ax[1, 1].set_xlim(xmin=0, xmax=4)
ax[1, 1].legend()
ax[1, 1].grid()  # включение отображение сетки

plt.show()
