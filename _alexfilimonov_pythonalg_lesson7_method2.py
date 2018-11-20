#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
#отсортированный массивы.

import random
import decimal

list_size = int(input("Enter list size - integer number > 0:"))
li = []
for i in range(list_size):  
    #li.append(random.randint(0, 50))
    li.append(float(decimal.Decimal(random.randrange(0,5000)))/100)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
    if len(list) < 2:
        return list
    middle = int(len(list) / 2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)

print("List before sorting - ", li)
li = mergesort(li) 
print("List after sorting - ", li)


