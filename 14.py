# модификаторы доступа
# r - read(считывание информации)
# w - write(запись)
# a - append(дозапись)
# x - открытие файла для записи если он не существует
# r+ w+ a+
# b - binary rb wb ab
# запись и дозапись в файл
# f = open('test.txt', 'w', encoding='utf-8')
# # f.write(str(23) + '\n')
# # f.write("мир" + "\n")
# # f.close()
# считывание из файла
# f = open('test.txt', 'r', encoding='utf-8')
# s = f.read()
# f.close()
# s = s.replace("\n",' ').rstrip()
# print(s)
# print(repr(s))
# student = []
# f = open('test.txt', 'r', encoding='utf-8')
# for i in range(3):
#     s = f.readline().rstrip().split()
#     s = list(map(int,s))
#     # for j in range(len(s)):
#     #     s[j] = int(s[j])
#     student.append(s)
# f.close()
# print(student)
# student = []
# f = open('test.txt', 'r', encoding='utf-8')
# for line in f:
#     line = line.rstrip().split()
#     line = list(map(int, line))
#     student.append(line)#extend
#     print(line)
# f.close()
# print(student)
# f = open('test.txt', 'r', encoding='utf-8')
# lst = f.readlines()
# f.close()
# for i in range(len(lst)):
#     lst[i]=lst[i].rstrip()
#
# print(lst)


# students = {}
# with open('test.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         space = line.index(" ")
#         key = line[:space]
#         value = line[space + 1:].rstrip().split()
#         value = list(map(int, value))
#         students[key] = value
#
# print(students)
# for key,value in students.items():
#     summa = sum(value)
#     avg = summa / len(value)
#     value.append(avg)
#
# with open('students.txt','w',encoding="utf-8") as fstud:
#     for key in students:
#         fstud.write(key+" "+ str(students[key][-1]) +"\n")
# 1 Exeption
# try:
#     x = (1, 2, 5, 7)
#     x = x  / 2
#     print(x)
# except TypeError:
#     print("Type error ;(")
# 12.	Дана строка. Пользователь ищет в ней подстроку.
# Если подстрока не найдена то бросьте ValueError
s = input()
sb_str = input()
if sb_str not in s:
    raise NameError("sb_str not found in s")