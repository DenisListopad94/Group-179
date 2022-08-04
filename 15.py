# import os
# print(dir(os))
# os.rename("test.txt","test1.txt")
# print(os.getcwd())
# os.mkdir("folder")
# os.chdir("folder")
# print(os.getcwd())
# os.chdir("..\..")
# print(os.getcwd())
# os.makedirs("f1/f2/f3")
# os.chdir("f1/f2/f3")
# print(os.getcwd())
# os.remove("lesson1.py")
# os.rmdir('folder')
# os.removedirs('f1/f2/f3')
# os.mkdir("f1")
# os.chdir('f1')
# open('test.txt','w')
# os.remove('test.txt')
# os.chdir('..')
# os.rmdir('f1')
# print(help(os.replace))
# os.mkdir('folder')
# os.replace('students1.txt','students2.txt')
# tup = (4,15)
# print(tup.index(4))
# lst = [5, 6, 8, 1]
# lst.append(7)
# lst.insert(1,19)
# del lst[0]
# lst.pop(4)
# lst.remove(19)
# lst.clear()
# lst.reverse()
# lst.sort(reverse=True)
# lst.extend([6,2,6,1])
# lst4 = lst
# lst2 = lst.copy()
# lst3 = lst[:]
# print(id(lst2))
# print(id(lst3))
# print(id(lst))
# print(id(lst4))
# set1 = {5, 2, 6}
# set1.add(7)
# set1.update([5, 7, 2, 0, 1, 3])
# set1.pop()
# set1.remove(7)
# set1.clear()
# print(set1)
# d = {'Vasya': 38, 23: [5, 2, 6, 2]}
# d.update({7: 98})
# d['Kolya'] = 27
# d.pop(7)
# d.popitem()
# print(d.get(23))
# print(d)
# d1 = {}
# print(d1.fromkeys([1,2,3],100))
# for key in d:
#     print(key,d[key])
# for value in d.values():
#     print(value)
# for key,value in d.items():
#     print(key,value)
# for key, value in d.items():
#     if isinstance(value, list):
#         print(key, *value)
#     else:
#         print(key, value)
# d = {"очи": "глаза", "лик": "лицо", "перст": "палец"}
# word = input("enter word: ")
# for key, value in d.items():
#     if key == word:
#         print(value)
#         break
#     if value == word:
#         print(key)
#         break
# else:
#     print(f"синонима к слову {word} в нашем словаре нет")
# 4 matrix
# lst = [[1]*6 for i in range(6)]
# for i in range(6):
#     for j in range(6):
#         if i==0 or j==0:
#             continue
#         else:
#             lst[i][j]= lst[i-1][j] +lst[i][j-1]
#
# for i in range(6):
#     print(*lst[i])
# 5matrix
# lst = [[(i+1)**(j+1) for i in range(5)] for j in range(4)]
# for i in range(4):
#     print(*lst[i])
# 16 matrix
# n = int(input())
# lst = [[(i+1)+(j*n) for i in range(n)] for j in range(n)]
# lst2 = []
# for i in range(n):
#     if i %2==0:
#         lst2.append(lst[i])
#     else:
#         lst2.append(lst[i][::-1])
# for i in range(n):
#     print(*lst2[i])
# 6.	Имеется текстовый файл.
# -Найти длину самой длинной строки.
# -Найти номер самой длинной строки. Если таких строк несколько, то найти номер одной из них.
# -Напечатать самую длинную строку. Если таких строк несколько, то напечатать первую из них.
# with open("students2.txt", 'r') as f:
#     max_len = 0
#     max_ind = 0
#     str_max = ""
#     ind = 1
#     for line in f:
#         line = line.rstrip()
#         if len(line) > max_len:
#             str_max = line[:]
#             max_ind = ind
#             max_len = len(line)
#         ind += 1
# print(max_len)
# print(max_ind)
# print(str_max)
#
# import random
#
# n=random.randint(2,4)
# m=random.randint(2,5)
# A=[]
# for k in range(n):
#     lst=([int (f) for f in input(f"введите {m} чисел строки через пробел:").split()])
#     A.append(lst)
# c=m
# for j in range (m):
#     for i in range (len(A)):
#         print((A[i][c-1]),end=' ')
#     c-=1
#     print()
# lst = [int(s) for s in input().split()]
# count = 0
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)
print("hello")