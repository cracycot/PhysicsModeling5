import numpy as np
import matplotlib.pyplot as plt


def projectile_motion(v0, angle, h0, k, t_max=10, dt=0.01):
    """
    Моделирует движение тела, брошенного под углом с учетом силы сопротивления воздуха.

    Параметры:
    v0 : float  - начальная скорость (м/с)
    angle : float - угол в градусах
    h0 : float - начальная высота (м)
    k : float - коэффициент сопротивления воздуха
    t_max : float - максимальное время моделирования (с)
    dt : float - шаг по времени (с)
    """
    g = 9.81  # ускорение свободного падения, м/с^2

    # Начальные условия
    angle_rad = np.radians(angle)
    vx0 = v0 * np.cos(angle_rad)
    vy0 = v0 * np.sin(angle_rad)

    # Инициализация массивов
    n_steps = int(t_max / dt)
    x = np.zeros(n_steps)
    y = np.zeros(n_steps)
    vx = np.zeros(n_steps)
    vy = np.zeros(n_steps)

    # Начальные значения
    x[0], y[0] = 0, h0
    vx[0], vy[0] = vx0, vy0

    # Метод Рунге-Кутты 4-го порядка
    for i in range(1, n_steps):
        kx1 = dt * vx[i - 1]
        ky1 = dt * vy[i - 1]
        kvx1 = dt * (-k * vx[i - 1])
        kvy1 = dt * (-g - k * vy[i - 1])

        kx2 = dt * (vx[i - 1] + kvx1 / 2)
        ky2 = dt * (vy[i - 1] + kvy1 / 2)
        kvx2 = dt * (-k * (vx[i - 1] + kvx1 / 2))
        kvy2 = dt * (-g - k * (vy[i - 1] + kvy1 / 2))

        kx3 = dt * (vx[i - 1] + kvx2 / 2)
        ky3 = dt * (vy[i - 1] + kvy2 / 2)
        kvx3 = dt * (-k * (vx[i - 1] + kvx2 / 2))
        kvy3 = dt * (-g - k * (vy[i - 1] + kvy2 / 2))

        kx4 = dt * (vx[i - 1] + kvx3)
        ky4 = dt * (vy[i - 1] + kvy3)
        kvx4 = dt * (-k * (vx[i - 1] + kvx3))
        kvy4 = dt * (-g - k * (vy[i - 1] + kvy3))

        x[i] = x[i - 1] + (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
        y[i] = y[i - 1] + (ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6
        vx[i] = vx[i - 1] + (kvx1 + 2 * kvx2 + 2 * kvx3 + kvx4) / 6
        vy[i] = vy[i - 1] + (kvy1 + 2 * kvy2 + 2 * kvy3 + kvy4) / 6

        if y[i] < 0:  # тело достигло земли
            y[i] = 0
            break

    time = np.linspace(0, i * dt, i)

    # Построение графиков
    plt.figure(figsize=(12, 8))

    # Траектория движения
    plt.subplot(3, 1, 1)
    plt.plot(x[:i], y[:i], label='Траектория движения')
    plt.xlabel("Расстояние (м)")
    plt.ylabel("Высота (м)")
    plt.title("Траектория движения тела")
    plt.grid(True)
    plt.legend()

    # Зависимость скорости от времени
    plt.subplot(3, 1, 2)
    speed = np.sqrt(vx[:i] ** 2 + vy[:i] ** 2)
    plt.plot(time, speed, label='Скорость тела', color='g')
    plt.xlabel("Время (с)")
    plt.ylabel("Скорость (м/с)")
    plt.title("Зависимость скорости от времени")
    plt.grid(True)
    plt.legend()

    # Зависимость координат от времени
    plt.subplot(3, 1, 3)
    plt.plot(time, x[:i], label="Координата x", color='b')
    plt.plot(time, y[:i], label="Координата y", color='r')
    plt.xlabel("Время (с)")
    plt.ylabel("Координата (м)")
    plt.title("Зависимость координат от времени")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


# Ввод параметров с консоли с проверкой корректности
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Некорректный ввод! Пожалуйста, введите число.")


def get_angle_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 90:
                return value
            else:
                print("Угол должен быть в диапазоне от 0 до 90 градусов.")
        except ValueError:
            print("Некорректный ввод! Пожалуйста, введите число.")


# Получение входных данных
v0 = get_float_input("Введите начальную скорость (м/с): ")
angle = get_angle_input("Введите угол броска (в градусах от 0 до 90): ")
h0 = get_float_input("Введите начальную высоту (м): ")
k = get_float_input("Введите коэффициент сопротивления среды: ")

# Запуск моделирования
projectile_motion(v0, angle, h0, k)
