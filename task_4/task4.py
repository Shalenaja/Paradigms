"""
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.
"""

# решение в рамках  функциональной парадигмы, т.к.задача связана с математическими фактами
from math import sqrt
from statistics import mean, variance


def s1(data1, data2):
    avg1 = mean(data1)
    avg2 = mean(data2)
    sum = 0
    i = 0
    while i <= len(data1)-1:
        a = dataX[i] - avg1
        b = dataY[i] - avg2
        c = a * b
        sum += c
        i += 1
    return sum

def s2(data1, data2):
    avg1 = mean(data1)
    avg2 = mean(data2)
    sum1 = 0
    sum2 = 0
    sqr = 0
    i = 0
    while i <= len(data1)-1:
        a = (dataX[i] - avg1) ** 2
        b = (dataY[i] - avg2) ** 2
        sum1 += a
        sum2 += b
        mult = sum1 * sum2
        i += 1
    sqr += sqrt(mult)
    return sqr

def s3(data1, data2, s1, s2):
    return s1(data1, data2) / s2(data1, data2)

dataX = [1, 12, 3, 4, 15, 6]
dataY = [6, 7, 8, 9, 10, 11]
print(s3(dataX, dataY, s1, s2))