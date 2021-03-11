'''
Задан список целых чисел. Напишите функцию, которая возвращает наибольшую сумму 
несмежных чисел. Числа могут быть 0 или отрицательными. Например, для списка 
[2, 4, 6, 8] функция должна возвращать 12, поскольку мы выбираем 4 и 8. Для 
[5, 1, 1, 5] должна вернуть 10, поскольку мы выбираем 5 и 5.
'''
def get_largest_non_adj_sum(array):
    previous, largest = 0, 0
    for amount in array:
        print("amount: {}; previous: {}; largest: {}".format(amount, previous, largest))
        previous, largest = largest, max(largest, previous + amount)
        print("new_previous: {}; new_largest: {}".format(previous, largest))
    return largest
