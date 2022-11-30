# list = [[j for j in range(3)]for i in range(4)]
# print(list)

r,c = (5,5)
# list = [[0]*c]*r
# print(list)
# list = [[0]*c]*r
# list[0][0] = 1
# print(id(list[0]))
# print(id(list[1]))

# list = [[0 for i in range(5)]for i in range(5)]
# # print(id(list[0]))
# # print(id(list[1]))
# list[0][1] = 1
# print(list)

# list = [[1,2,3],[4,5],[6,7,8]]
# new_list = [sublist for val in  list for sublist in val]

# print(new_list)

list = [["hello","world"],["mango","banana"],["python","java"]]
new_list = [sublist for val in  list for sublist in val if len (sublist) > 3]
print(new_list)