#      0  1     2
# lst = [5, 2, [6, 2, 1]]
#           0          1
#        0  1  2    0  1  2
# lst2 = [[5, 2, 1], [6, 1, 8]]
# print(lst2[0])
# print(lst2[0][2])
# for i in range(len(lst2)):
#     for j in range(len(lst2[i])):
#         print(lst2[i][j],end=" ")
#     print()
# 1 cпособ
# lst = []
# for i in range(3):
#     lst2 = [int(i) for i in input().split()]
#     lst.append(lst2)
# print(lst)
# 2 способ
# lst = [[int(i) for i in input().split()] for i in range(3)]
# print(lst)
# 3 способ
# lst = [list(map(int,input().split())) for i in range(3)]
# print(lst)
# row = column = 4
# lst = [[1 for _ in range(column)] for _ in range(row)]
# lst2 = [[1]*column for _ in range(row)]
# print(lst)
# print(lst2)
# lst = [[i * j for i in range(3) if j % 2 == 0] for j in range(5)]
# print(lst)
# lst = [[int(i) for i in input().split()] for i in range(3)]
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         if i > j:
#             print(lst[i][j], end=" ")

# lst = [[int(i) for i in input().split()] for i in range(4)]
# summa = 0
# for i in range(4):
#     summa +=sum(lst[i])
# print(summa)
# поиск строки с максимальным числом чётных элементов
# lst = [[int(i) for i in input().split()] for i in range(4)]
# number_row = -1
# flag = False
# max_count = 0
# for i in range(len(lst)):
#     count = 0
#     for j in range(len(lst[i])):
#         if lst[i][j] % 2 ==0:
#             count += 1
#     if count > max_count:
#         flag = True
#         max_count = count
#         number_row = i
#
# if flag:
#     print("row:",number_row)
# else:
#     print("no row")
# поиск столбца с максимальным числом чётных элементов
# max_count = 0
# number_row = -1
# flag = False
# lst = [[int(i) for i in input().split()] for i in range(4)]
# for i in range(len(lst)):
#     count = 0
#     for j in range(len(lst[i])):
#         if lst[j][i] % 2 == 0:
#             count += 1
#     if count > max_count:
#         flag = True
#         max_count = count
#         number_row = i
# if flag:
#     print("row:",number_row)
# else:
#     print("no row")
# нахождение всех простых чисел матрицы
# import random
# import random
#
# lst = [[random.randint(2,20) for i in range(5)] for j in range(5)]
# lst2 = []
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j],end=" ")
#         for k in range(2,lst[i][j]):
#             if lst[i][j] % k == 0:
#                 break
#         else:
#             lst2.append(lst[i][j])
#     print()
#
# print(lst2)
# exception
# lst = [2,5,1]
# try:
#     print(6/0)
# except ZeroDivisionError:
#     print("ZeroDivisionError :(")
# except TypeError:
#     print("Type Error ;(")
# except IndexError:
#     print("Index Error :(")
# except Exception as e:
#     print(e)
#     print(type(e))
# else:
#     print("all good")
# finally:
#     print("always")
# raise - кидает ошибку
# while True:
#     try:
#         name = input()
#         if name[0].islower():
#             raise NameError("Имя должно быть написано с большой буквы")
#         else:
#             print(f"hello {name}")
#             break
#     except NameError:
#         print("Введите имя заново")
# 5 задача
# lst = [str(i) for i in input().split()]
# print(len(lst) - len(set(lst)))
# 6 задача
# import random
#
# number = int(input())
# n = random.randint(1, number)
# set1 = set(range(1, number + 1))
# print(n)
# count = 0
# while True:
#     print(*set1)
#     guess = {int(i) for i in input("Enter guess:").split()}
#     if n in guess and len(set1) > 1:
#         print("Yes:", end="")
#         set1 = guess
#         count += 1
#     else:
#         set1.difference_update(guess)
#         count += 1
#     if len(set1) == 1:
#         print(f"you guess for {count} time")
#         break
# 4 задача
lst = [int(i) for i in input().split()]
set1 = set()
for elem in lst:
    if elem not in set1:
        print("NO")
        set1.add(elem)
    else:
        print("YES")