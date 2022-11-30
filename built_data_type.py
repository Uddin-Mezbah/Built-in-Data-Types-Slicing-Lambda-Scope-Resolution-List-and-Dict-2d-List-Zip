# int , float,
# string,tuple,list
# dictionary,
# set

# a = 120000000000000000007777777777777.988888888888888888888
# print(a+1)

# list = [1,2,3,4,5,6,7,2,3,45,4,4,5,2,2,]
# list2 = [1,2,3,4,5,6,7,2,3,45,4,4,5,2,2,]

# print(list[0])
# print(list[-1]) #revers index
# print(list.count(2)) #count value
# print(list+list2) #add 2 list

#nested loop

list = [1,2,3,4,[5,6,[7,8,[11,12,[13,[13,14]]]]]]

print(1 in list)
# print(list[4][2][2][2][0])
# list.append(100)
# list.extend([0,1,2])
# print(list)
# print(list)

# list[4][2][2][2][0] = 13*2
# print(list)

# tp = (1,2,3,4,5,[1,2,3,4])
# # tp[0] = 4
# tp[5][0] = 13
# # tp[5]= 13 #change list
# print(tp)

#dictonary

# dct = {"rahim": 12000,"karim": 20000}
# # print(dct['halim'])
# # print(dct.get("rahim"))
# # print(dct.get("halim",False))

# child1 = {
#     "name" : "jack",
#     "year" : "2022"
# }
# child2 = {
#     "name" : "mack",
#     "year" : "2020"
# }
# child3 = {
#     "name" : "nck",
#     "year" : "2019"
# }

# myfamily = {
#     "child1" : child1,
#     "child2" : child2,
#     "child3" : child3

# }

# # print(myfamily["child1"]['name'])
# print(myfamily.get('child2',False).get('year',False))

# a = dict([(1,'a'),(2,'a'),(3,'a'),(4,'a'),(6,'a')])
# print(a)
# a.pop(3)
# print(a)
# print(a.keys())
# print(a.values())

# for key,value in a.items():
#     print(f"key {key} : value {value}")

#set
# st = [1,2,3,4,5]
# st.insert(0,3)
# print(st)

#string

str = "3 i love python" #3 is memoric value
# str[0] = 'I'
print(str)
# print(str[::-1])
print(str.upper())
print(str.lower())
print('love' in str)
# print(str[0].isalpha())
print(str[0].isalnum())