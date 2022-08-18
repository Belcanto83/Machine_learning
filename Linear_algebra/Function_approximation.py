import numpy as np
from scipy import linalg
from matplotlib import pylab as plt


# Аппроксимируемаемая(исходная) функция
def f(x):
    return np.sin(x/5)*np.exp(x/10) + 5*np.exp(-x/2)


# Исходные данные, которые нужно задать! Остальное считается автоматически.
n = 3  # Степень приближающего многочлена
x_init = np.array([1, 4, 10, 15])  # Значения переменной "x", по которым строим нашу аппроксимацию исходной функции


# Аппроксимирующая(приближающая) функция многочленом n-й степени
def approx_f(w, x):
    result_sum = 0
    for i in range(n+1):
        result_sum += w[i]*x**i
    return result_sum


# Аппроксимируем функцию f(x) многочелном первой степени
y = f(x_init)
x_vector = [x_init ** i for i in range(n + 1)]
matrix = np.array(x_vector).T
print('matrix:')
print(matrix)
print('y: ', y)

w_found = linalg.solve(matrix, y)
print('w_found: ', w_found)

x_r = np.arange(1, 15, .1)
y_r = f(x_r)
plt.plot(x_r, y_r)

y_approx = approx_f(w_found, x_r)
plt.plot(x_r, y_approx)

plt.show()
