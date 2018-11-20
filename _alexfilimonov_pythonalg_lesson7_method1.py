#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
#заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и
#отсортированный массивы. Сортировка должна быть реализована в виде функции. По
#возможности доработайте алгоритм (сделайте его умнее).

import random

def sort_bubble(li):
    n = 1
    while n < len(li):
        for i in range(len(li)-n):
            if (li[i] < li[i+1]) :
                li[i],li[i+1] = li[i+1],li[i]
        n += 1
    return li

list_size = int(input("Enter list size - integer number > 0:"))
li = []
for i in range(list_size):  
    li.append(random.randint(-100, 100))
print("List before sorting - ", li)
li = sort_bubble(li) 

print("List after sorting - ", li)

