from math import *


def prime(length):
    array = [True] * (ceil(length * log(length)) + 2)
    array[0] = False
    array[1] = False
    for i in range(2, len(array)):
        if array[i]:
            for j in range(i * 2, len(array), i):
                array[j] = False
    ans = []
    for i in range(len(array)):
        if array[i]:
            ans.append((i, i))
    return ans


def all_numbers(length):
    return [(i, i) for i in range(length)]


def fibonacci(length):
    ans = [(1, 1), (2, 2)]
    for i in range(length - 2):
        x = ans[-1][0] + ans[-2][0]
        ans.append((x, x))
    return ans
