'''
Задан массив целых чисел и число k, где 1 <= k <= длина массива, вычислите 
максимальные значения каждого подмассива длины k.
'''

from collections import deque

def get_sliding_max(a, k):

    
    window_max_elements = list()

    if not a:
        return None
    if len(a) <= k:
        return max(a)

    dq = deque()
    # окно длины к на массив с нуля до к
    # выбрать больший элемент
    # сдвинуть на единицу вправо слева выкинуть, справа добавить
    # другой срез выбратт больший элемент
    # пока конечный элемент не среза не станет посл в массиве

    for i in range(k):
        while dq and a[dq[-1]] < a[i]:
            dq.pop()
        dq.append(i)

    window_max_elements.append(a[dq[0]])

    for i in range(k, len(a)):
        while dq and dq[0] <= i-k:
            dq.popleft()

        while dq and a[dq[-1]] < a[i]:
            dq.pop()
        dq.append(i)

        window_max_elements.append(a[dq[0]])
    return window_max_elements