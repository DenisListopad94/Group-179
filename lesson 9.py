# 3.	Задан список из k чисел. Определить количество инверсий в списке (т. е. таких пар элементов,
# в которых большее число находится слева от меньшего).
# import random
#
# k = int(input("enter k:"))
# lst = []
# for i in range(k):
#     lst.append(random.randint(1, 10))
# print(lst)
# count = 0
# for i in range(k - 1):
#     if lst[i] > lst[i + 1]:
#         count += 1
# print(count)
# 2.	Задано два списка. Найти наименьшие среди элементов первого списка, которые не входят во второй список.
# lst1 = [4, 3, 10, 1]
# lst2 = [1, 4, 8, 9]
# lst3 = []
# for elem in lst1:
#     if elem not in lst2:
#         lst3.append(elem)
# if len(lst3)!=0:
#     print(min(lst3))
# else:
#     print("not found")
# lst1 = [4, 8, 5, 1]
# lst2 = [1, 4, 8, 9, 6, 7]
# m = max(lst1)
# for elem in lst1:
#     if elem not in lst2:
#         if elem < m:
#             m = elem
# if m not in lst2:
#     print(m)
# else:
#     print("not found")
# 5.	Дан список положительных целых чисел . Вставить после каждого чётного числа его перевёртыш
# lst = [1, 15, 28, 100, 13, 6]
# # 1 15 28 82 100 1 13 6 6
# i = 0
# while i < len(lst):
#     if lst[i] % 2 == 0:
#         temp = str(lst[i])[::-1]
#         temp = int(temp)
#         lst.insert(i + 1, temp)
#         i += 1
#     i += 1
# print(lst)
# 6.	Дан список . Вычислить сколько раз в нем встречается каждый элемент, не используя сортировки
# lst = [5, 2, 7, 1, 2, 7, 8, 1, 1]
# for elem in lst:
#     print(elem,"встречается",lst.count(elem),"раз(а)")
# for i in range(len(lst)):
#     if lst.index(lst[i]) == i:
#         print(lst[i], "встречается", lst.count(lst[i]), "раз(а)")
# 7.	Дан список . Перезаписать его так,
# чтобы сначала были все положительные числа, а затем все отрицательные и нули, сохраняя порядок их следования.
# lst = [-5, 6, 8, -1, 0, 5, 7, -8]
# print(lst.__sizeof__())
# for i in range(len(lst)):
#     if lst[i] < 0:
#         for j in range(i + 1, len(lst)):
#             if lst[j] > 0:
#                 lst[i], lst[j] = lst[j], lst[i]
#                 break
#     if lst[i] == 0:
#         lst[i],lst[-1] = lst[-1],lst[i]
# print(lst)
# 4.	Программе подаётся на вход произвольная строка. Удалите из нее повторяющиеся символы
# (т. е. символы, встречающиеся в строке во второй или более раз) и выведите результат на экран.
# Задачу решить через список. Функцию set не использовать
# s = "Xa-xa-xa-xa"
# lst = list(s)
# lst2 = []
# for elem in lst:
#     if elem not in lst2:
#         lst2.append(elem)
# print("".join(lst2))
# i = 0
# while i < len(lst):
#     if lst.count(lst[i]) > 1:
#         lst.remove(lst[i])
#         continue
#     i += 1
# print("".join(lst))
# 9.	Дан список . Перезаписать его так, чтобы чётные элементы чередовались с нечётными
# lst = [4, 5, 6, 6, 8, 7, 7, 8, 2, 2, 9]
# for i in range(len(lst)):
#     if i % 2 == 0 and lst[i] %2 == 1:
#         for j in range(i+1,len(lst)):
#             if lst[j] % 2 == 0:
#                 lst[i],lst[j] = lst[j],lst[i]
#                 break
#
#     if i % 2 == 1 and lst[i] %2 == 0:
#         for j in range(i+1,len(lst)):
#             if lst[j] % 2 == 1:
#                 lst[i],lst[j] = lst[j],lst[i]
#                 break
# print(lst)
# lst = [4, 6, -6, 7, -1, -8, -9]
# lst2 = ["asf", 'fefsy', 'poos', 'aa']
# lst.append(5)
# lst.insert(1,9)
# lst.remove(6)
# k = lst.pop(0)
# del lst[0:3]
# lst.extend([8,5,2])
# lst += [6,3,1]
# lst.clear()
# lst.reverse()
# lst.sort(key = abs ,reverse=True )
# lst2.sort(key = len, reverse = True)
# lst.sort(key=lambda x: not x % 2)
# lst2.sort(key=lambda x: x[-1])
# print(lst2)
# lst = []
# s = input()
# while s != ".":
#     if "POST" in s:
#         # s = s.split()[1:]
#         # lst.append(" ".join(s))
#         ind = s.find(" ")
#         s = s[ind + 1:]
#         lst.append(s)
#     elif "GET" in s:
#         if lst:
#             print(lst[-1])
#     elif "DELETE" in s:
#         if lst:
#             lst.pop()
#     s = input()
# print(lst)
# list comprehension
# [что положить в список for из чего положить in диапазон значений(итерируемый объект)]
# [что положить в список for из чего положить in диапазон значений(итерируемый объект) if условие верно]
# [что положить в списое if условие верно else что положить for из чего положить in диапазон значений(итерируемый объект)]

# import random

# lst = [i for i in range(1,11)]
# lst2 = [i for i in "hello world"]
# lst3 = [int(input()) for i in range(5)]
# lst4 = [random.randint(1,100) for i in range(5)]
# lst5 = [int(i) for i in input().split()]
# lst2 = [i for i in "hello2319 12 world" if i.isalpha() or i ==" "]
# lst = [i for i in range(1, 101) if i % 2 == 0 and i % 5 == 0]
# lst = [i if i % 2 == 0 else i ** 3 for i in range(1, 11)]
# print(lst)
# 10==============================================
# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

# gl = "aeyuio"
# count_gl = count_sgl = 0
#
# lst = [15, 48, 'hello', 692, 19, 'world']
# for i in range(len(lst)):
#     if type(lst[i]) == int:
#         if lst[i] % 2 == 0:
#             k = list(str(lst[i]))
#             summa = sum(list(map(int, k)))
#             print(summa)
#         else:
#             lst[i] = 1
#     if type(lst[i]) == str:
#         for elem in lst[i]:
#             if elem in gl:
#                 count_gl += 1
#             elif elem.isalpha():
#                 count_sgl += 1
# print(lst)
# print(count_gl, count_sgl)
# tup = (6, 3, 2, [6, 3, 1])
# tup1 = ()
# tup[3].clear()
# tup = tup[:-1]
# print(tup1.__sizeof__())
# tup = (5, 6, "hello", [5, 2, 6], (7, 8, 9), 5)
# print(tup)
# for i in range(len(tup)):
#     print(tup[i])
# for elem in tup:
#     print(elem)
# for ind,elem in enumerate(tup):
#     print(ind,elem)
# print(tup.count(5))
# print(tup.index([5, 2, 6]) )
# print(len(tup[3]))
# if 4 in tup:
#     print("yes")
# else:
#     print("no")
# s = "hello world"
# tup1 = tuple(list(map(int,input().split())))
# tup2 = tuple(s)
# tup3 = tuple(range(1,11))
# tup4 = tuple([i**3 for i in range(1,6)])
#
# print(tup1)
# print(tup2)
# print(tup3)
# print(tup4)
# tup1 = (1,2,4)
# tup2 = (5,6,2)
# tup3 = tup1 + tuple("221321")
# print(tup3)
# tup4 = tup2*3
# print(tup4)
# a = (input ("enter a"))
# Tup = tuple(a)
# print(Tup)
# s = input()
# tup = tuple(s.split())
# print(tup)
# tup = ("Vasya", "Pupkin", 5.23)
# name, surname, age = tup
# print(name, surname, age)
# Создайте кортеж из случайных 10 чисел. Найдите его максимальный минимальный элемент
# import random
# tup = tuple([random.randint(1,10) for i in range(10)])
# print(tup)
# print(max(tup),min(tup))
# 4.Дан список, упорядоченный по не убыванию элементов в нем. Определите, сколько в нем различных элементов
# alt + ctrl + L
# lst = [1, 1, 2, 4, 7, 7, 7, 8, 9, 9, 9, 11, 15]
# lst = [1,1,1,1,1]
# count = 1
# for i in range(len(lst) - 1):
#     if lst[i] != lst[i + 1]:
#         count += 1
# print(count)
# 5.	Программа получает на вход три числа через пробел — начало и конец диапазона,
# а также степень, в которую нужно возвести каждое число из диапазона.
# Выведите числа получившегося списка через пробел.
# a, b, step = map(int, input().split())
# print([i ** step for i in range(a, b + 1)])
# 6
# lst = [1]
#
# if len(lst) == 1:
#     print(lst[0])
# else:
#     for i in range(len(lst)):
#         if i ==len(lst)-1:
#             print(lst[0]+lst[i-1],end=' ')
#             continue
#         print(lst[i-1]+lst[i+1],end=' ')

# 8.	Дан список, состоящий из строк. Отсортировать его по длине слов.
# Сначала должны идти длинные слова затем короткие.
# lst = ["dasdas", 'asdas', 'das', 'sdadasfasf', 's']
# lst.sort(key=len, reverse=True)
# print(lst)
# 9.Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a'
# lst = ['sdsa','fdsaaa',"dgf",'saege']
# lst.sort(key = lambda x: x.count("a"))
# print(lst)
# 10
# lst = [4, 8, 0, 3, 4, 2, 0, 3]
# for i in range(len(lst)):
#     if lst.count(lst[i]) >= 2 and lst.index(lst[i]) == i:
#         print(lst[i], end=" ")
# Сгенерировать список всех простых чисел до  100 с помощью генератора.
# lst = [i for i in range(2, 100) if
#        i == 2 or i == 3 or i == 5 or i == 7 or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0)]
# print(lst)
# lst = [i for i in range(2, 100) if len([j for j in range(2, i) if i % j == 0]) == 0]
# print(lst)
# Дан список , преобразуйте исходный список, вставив 0 между числами. Дополнительный список не создавать!
# lst = [1, 2]
# i = 0
# while len(lst) > i:
#     if i % 2 == 1:
#         lst.insert(i,0)
#     i+=1
# print(lst)
# lst = []
# n = int(input())
# for i in range(1,n):
#     if len(lst) >=n:
#         lst = lst[:n]
#         print(lst)
#         break
#     print(i)
#     k = str(i) * i
#     lst.extend(list(map(int,k)))
