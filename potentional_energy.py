import numpy as np
import matplotlib.pyplot as plt


def elasticity_force(x, y, k=1.0):
    """ Возвращает потенциальную энергию для силы упругости F = -k * r. """
    r = np.sqrt(x ** 2 + y ** 2)
    return 0.5 * k * r ** 2


def gravity_force(x, y, m=1.0, g=9.81):
    """ Возвращает потенциальную энергию для силы тяжести F = m * g. """
    return m * g * y


def custom_force(x, y, a=1.0, b=1.0):
    """ Возвращает потенциальную энергию для произвольной силы вида F = -a * x^n - b * y^m. """
    n, m = 2, 2  # степенные коэффициенты по осям x и y
    return a * x ** n + b * y ** m


def calculate_potential_energy(x, y, force_type):
    """ Вычисляет потенциальную энергию для выбранного типа силы. """
    if force_type == 'elasticity':
        return elasticity_force(x, y)
    elif force_type == 'gravity':
        return gravity_force(x, y)
    elif force_type == 'custom':
        return custom_force(x, y)
    else:
        raise ValueError("Неизвестный тип силы.")


def get_force_type():
    """ Ввод типа силы с консоли. """
    print("Выберите тип силы для моделирования потенциального поля:")
    print("1: Сила упругости")
    print("2: Сила тяжести")
    print("3: Произвольная сила в виде степенной функции")

    while True:
        choice = input("Введите номер выбранной силы (1-3): ")
        if choice == '1':
            return 'elasticity'
        elif choice == '2':
            return 'gravity'
        elif choice == '3':
            return 'custom'
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")


# Ввод параметров
force_type = get_force_type()

# Задаем диапазон координат
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Рассчитываем потенциальную энергию
U = calculate_potential_energy(X, Y, force_type)

# Визуализация распределения потенциальной энергии
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, U, cmap='viridis')
plt.colorbar(label="Потенциальная энергия U(x, y)")
plt.title("Распределение потенциальной энергии")
plt.xlabel("Координата x")
plt.ylabel("Координата y")
plt.grid(True)
plt.show()
