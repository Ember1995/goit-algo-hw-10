import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return 1 / x

# Межі інтегрування
a = 0.5 
b = 2

# Створення діапазону значень для x
x = np.linspace(0.1, 2.5, 400)
y = f(x)

# Інтегрування методом Монте-Карло
np.random.seed(0)  
N = 100000 

x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)

monte_carlo_result = (b - a) * np.mean(y_rand)

# Інтегрування методом quad
result, quad_error = spi.quad(f, a, b)

# Порівняння результатів
error_monte_carlo = np.abs(result - monte_carlo_result)

# Вивід результатів
print(f"{'Метод':<30} | {'Результат':<20} | {'Похибка':<20}")
print("-" * 75)
print(f"{'Монте-Карло':<30} | {monte_carlo_result:<20} | {error_monte_carlo:<20}")
print(f"{'Quad':<30} | {result:<20} | {quad_error:<20}")

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = 1/x від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
