#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
#в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
#одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
#Задачу можно решить без сортировки исходного массива. 

import random

def finding_mediana(li):
    n = len(li)
    for i in range(len(li)):
        N1=0 #qty of elements less than element with i-index of array li
        N2=0 #qty of elements more than element with i-index of array li
        for j in range(len(li)):
            if (j!=i and li[j]<li[i]) :
                N1+=1
            if (j!=i and li[j]>li[i]) :
                N2+=1
        if (N1 == N2) :
            print("Mediana is i=",i,"with value -",li[i], "Qty of elements less than mediana is", N1, "Qty of elements more than mediana is", N2)
            return
    print("Mediana is not found!")
    return

list_size = int(input("Enter list size - integer number > 0:"))
li = []
for i in range(2*list_size+1):  
    li.append(random.randint(0, 100))

print("List - ", li)
li = finding_mediana(li) 

