

'''
Площадь круга задана как r^2. Оцените число pi с точностью до 3 знаков после запятой, 
используя метод Монте-Карло.
Подсказка: основное уравнение круга: x ^ 2 + y ^ 2 = r ^ 2.
'''

from random import random

radius = 2

def estimate_pi(num_rand_tests):
    pi_counter = 0
    r_squared = radius ** 2

    for _ in range(num_rand_tests):
        x_rand = random() * radius
        y_rand = random() * radius

        if (x_rand ** 2) + (y_rand ** 2) < r_squared:
            pi_counter += 1

    return 4 * pi_counter/num_rand_tests

print(estimate_pi(1000))

