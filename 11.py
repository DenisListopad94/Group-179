# s = "hello"
# d = {(1):"one",2:"two"}
# d1 = {i:i for i in s}
# print(type(d))
# print(d1)
# d = dict([(1,5),(6,3)])
# d = {}
# d = d.fromkeys([5,2])
# print(d)
#    key value
# d = {1: "one", 2: "three"}
# print(d[2])
# for key in d:
#     print(key,d[key])
# for key,value in d.items():
#     print(key,value)

# if "one" in d.values():
#     print("yes")
# print(type(list(d.keys())))
# print(list(d.values()))
# d[3] = "three"
# print(d)
# d[3] = "tri"
# print(d)
# d.update({3:"three","four":4})
# print(d)

# d = {1: "one", 2: "three"}
# if 3 in d:
#     del d[3]
# print(d.get(2))
# print(d)

# d_phone = {"Vasya": [89312421], "Ira": 12957182}
# d_phone["Vasya"].append(17581221)
# print(d_phone)
# for key in d_phone:
#     print(key,":")
#     if type(d_phone[key]) is list:
#         print(*d_phone[key])
#     else:
#         print(d_phone[key])
# costumers = {
#     "Vasya" :{
#         "milk":2.31,
#         "pepsi":2.52,
#         "bread":5.25
#     },
#     "Ira":{
#         "butter":3.52,
#         "melon":6.25,
#         "watermelon":4.62
#     },
#     "Petya":{
#         "cheese":9.23,
#         "apple":4.21,
#         "chockolate":12.42
#     }
# }
# print(costumers)
# name = ""
# money = 0
# for key in costumers:
#     print(key, ":")
#     s = 0
#     for key2 in costumers[key]:
#         print(key2,"-",costumers[key][key2])
#         s += costumers[key][key2]
#     if money < s:
#         money = s
#         name = key
#     print("total:",s)
# print(f"the most generous is: {name}, he(she) sold {money}")
# lst_keys = [1,2,3]
# lst_values = ["one",'two',"three"]
# d = {}
# for i in range(len(lst_keys)):
#     d[lst_keys[i]] =lst_values[i]
# print(d)
# d = dict(zip([1,2,3],["one",'two',"three"]))
# print(d)
# product = {
#     "milk": [2.63, 100],
#     "butter": [3.21, 200],
#     'cheese gauda': [7.21, 20],
#     'yougurt': [1.52, 120],
#     'potato': [2.24, 1000],
#     'pasta': [4.25, 215]
# }
# money = 0
# while True:
#     s = input("name product or exit:")
#     if s == "exit":
#         break
#
#     if s in product:
#         count = int(input("count product:"))
#         if count <= product[s][-1]:
#             money += count * product[s][0]
#             product[s][-1] -= count
#         else:
#             print(f"not enough {count} {s}")
#     else:
#         print(f"no product {s} in shop")
#
# for key in product:
#     print(key, product[key][-1])
# print(money)