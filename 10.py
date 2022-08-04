# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.
# lst = [15, 48, 'hello', 6, 19, 'world', 2817487152]
# for elem in lst:
#     # if isinstance(elem,int)
#     if type(elem) is int:
#         if elem % 2 == 0:
#             s = str(elem)
#             lst2 = list(s)
#             summa = sum(list(map(int, lst2)))
#             print(summa)
#         else:
#             ind = lst.index(elem)
#             lst[ind] = 1
#     if isinstance(elem, str):
#         gl = sgl = 0
#         gl_letter ="aeyuio"
#         for sym in elem:
#             if sym in gl_letter:
#                 gl +=1
#             elif sym.isalpha():
#                 sgl +=1
#         print(gl,sgl)
#
# print(lst)
# tup = (5,2,2,[7,3,2,2],[7,3,2],"dsadas",(4,5,1,(4,2,5,1)),5)
# if 3 not in tup:
#     print("yes")
#
# for elem in tup:
#     print(elem)
# for i in range(len(tup)):
#     print(tup[i])
#
# for ind,elem in enumerate(tup):
#     print(ind,elem)

# import random
#
# s = 'hello world'
# tup1 = tuple(s)
# tup2 = tuple(range(1, 10))
# tup3 = tuple([random.randint(1, 100) for i in range(10)])
# print(tup1)
# print(tup2)
# print(tup3)
# 13.	С клавиатуры вводится натуральное число n <= 1000.
# Выведите n строк вида "На лугу n коров", склоняя слово
# "коров" в соответствии с числом n. Проверяем большие числа!!!
# n = int(input())
# for i in range(1,n+1):
#     if i % 10 == 1 and i %100 !=11:
#         # print("на лугу",i,"корова")
#         print("на лугу {} корова".format(i))
#     elif (i %10 == 2 and i %100 !=12) or (i %10 == 3 and i %100 !=13) or (i %10 == 4 and i %100 !=14):
#         print(f"на лугу {i} коровы")
#     else:
#         print(f"на лугу {i} коров")
# name = "Vasya"
# surname = "Pupkin"
# age = 24
#
# print(f"hello name {name} surname {surname} your age is {age}")
# print("hello name", name, "surname", surname, "your age is", age)
# 14.	Числа Фибоначчи – известная числовая последовательность,
# в которой первые два члена равны единице,
# а каждый последующий получается сложением двух предыдущих.
# По введенному числу n выведите n чисел Фибоначчи через пробел.
# a = 3
# b = 4
# print(a, b)
# buf = b
# b = a
# a = buf
# a, b = b, a
# print(a, b)
# a1 = a2 = 1
# n = int(input())
# if n == 1:
#     print(a1)
# elif n == 2:
#     print(a1, a2)
# else:
#     for i in range(1, n + 1):
#         print(a1, end=" ")
#         a1, a2 = a2, a1 + a2
# 16.	Даны натуральные числа n, m. Получить все числа меньше m взаимно простые с n.
# n, m = map(int, input().split())
# for i in range(n + 1, m + 1):
#     count = 0
#     for j in range(2, i):
#         if i % j == 0 and n % j == 0:
#             count += 1
#     if count == 0:
#         print(i,end=" ")
# 5.	Программа получает на вход три числа через пробел — начало и конец диапазона,
# а также степень, в которую нужно возвести каждое число из диапазона.
# Выведите числа получившегося списка через пробел.
# a, b, step = map(int, input().split())
# print([i ** step for i in range(a, b + 1)])
# 6 ================
# lst = [10]
# if len(lst) == 1:
#     print(*lst)
# else:
#     for i in range(len(lst)):
#         if i == len(lst) - 1:
#             print(lst[i - 1] + lst[0])
#             continue
#         print(lst[i - 1] + lst[i + 1], end=" ")
# 8.	Дан список, состоящий из строк.
# Отсортировать его по длине слов. Сначала должны идти длинные слова затем короткие.
# lst = ['23112', "fsdf", 'dsa', 'as']
# lst.sort(key=len, reverse=True)
# print(lst)
# 9.	Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a'
# lst = ['ads', 'asdaa', 'adaaaa', 'adfa']
# lst.sort(key = lambda x:x.count("a"))
# print(lst)
# print(bool([]))

# *Сгенерировать список всех простых чисел до  100 с помощью генератора.
# print([i for i in range(2, 100) if
#        i == 2 or i == 3 or i == 5 or i == 7 or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0)])
# print([i for i in range(2, 100) if not [j for j in range(2, i) if not i % j]])
# 12.	 Дан список , преобразуйте исходный список, вставив 0 между числами.
# Дополнительный список не создавать!
# lst = [6, 3, 6]
# lst = list(map(str, lst))
# s = '0'.join(lst)
# lst = list(s)
# lst = list(map(int, lst))
# print(lst)
# 13====================
# n = int(input())
# lst = []
# for i in range(1, n + 1):
#     print(i)
#     if len(lst) >= n:
#         break
#     s = str(i) * i
#     s = list(s)
#     s = list(map(int, s))
#     lst.extend(s)
# print(lst[:n])
s = input()
print(s)