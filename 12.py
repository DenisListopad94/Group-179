# d = {1: "one", 2: "two"}
# d2 = dict([(4, 2), (5, 7)])
# d3 = dict.fromkeys('hello',100)
# d4 = {i**2:i for i in [7,2,5] }
# print(d)
# print(d2)
# print(d3)
# print(d4)
# d = {1: "one", 2: "two"}
# d[3] = "three"
# d.update({4: 'four', 5: "five"})
# d[1] = 'one element'
# print(d)
# print(d.get(2,'no element'))
# del d[1]
# value = d.pop(3)
# print(value)
# print(d)
# d = {1: "one", 2: "two"}
# print(type(list(d.keys())))
# print(list(d.values()))
# print(d.items())
# d1 = d.copy()
# d.clear()
# if 'one' in d.values():
#     print("yes")
# print(d1)
# d = {1: "one", 2: "two"}
# for key in d:
#     print(key, d[key])
# for key, value in d.items():
#     print(key, value)
# costumers = {
#     "Vasya": {
#         "milk": 2.52,
#         "water": 4.25,
#         "apple": 2.62
#     },
#     "Petya": {
#         "orange": 7.12,
#         "melon": 5.15,
#         "pineapple":7.25
#     },
#     "Anna": {
#         "pepsi": 1.62,
#         "watermelon": 7.64,
#         "milk": 2.51,
#         "potato": 2.33
#     }
# }
# print(costumers)
# name_max = ""
# max_money = 0
# for name in costumers:
#     print("=======================")
#     money = 0
#     print(name,":")
#     for product in costumers[name]:
#         print(f"{product} - {costumers[name][product]}")
#         money += costumers[name][product]
#     if money > max_money:
#         name_max = name
#         max_money = money
#     print(f"money sold: {money}")
# print(f"{name_max} - {max_money} ")
# phone = {"Vasya": ["+721851251"], "Petya": ["+21512125","+74281758127","+127485712"], "Anna": "+21579122142"}
# print(phone["Vasya"])
# print(phone)
# phone["Vasya"][0] = "+24112512"
# phone["Vasya"].append("+421571512")
# print(phone)
# for key,value in phone.items():
#     print("========================")
#     print(key,":")
#     if type(value) is list:
#         for number in value:
#             print(number)
#     else:
#         print(value)
# zip
# d = dict(zip("hello",['one','two']))
# print(d)
# last task in presentation
# product = {
#     "melon": [200, 6.22],
#     "water": [500, 5.52],
#     "apple": [100, 6.21],
#     "cheese": [5, 52.52],
#     'butter': [20, 3.61]
# }
# summa = 0
# while True:
#     name_product = input("enter name product or exit:")
#     if name_product == "exit":
#         break
#     if name_product in product:
#         count = int(input(f"enter count {name_product}:"))
#         if count <= product[name_product][0]:
#             summa += product[name_product][1] * count
#             product[name_product][0] -= count
#         else:
#             print(f"not enoph {name_product} in shop. We have {product[name_product][0]},but you need {count}")
#     else:
#         print(f"no product name {name_product}")
#
# print(summa)

