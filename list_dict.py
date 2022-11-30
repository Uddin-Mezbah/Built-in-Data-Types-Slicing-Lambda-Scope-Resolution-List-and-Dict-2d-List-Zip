#list comphrension

# list = ["hello","world","python"]
# #expression for item in range

# list = ["hell","world","python"]
# new_list = [x.upper() for x in list]
# print(new_list)

#example - 2
# x = [i for i in range(1,10)]
# y = list(range(1,10))
# print(x)

#example-3

# x = "hello"
# y = [i for i in x]
# print(y)

#example 4

# list = [x for x in range(1,20) if x%2 == 0]
# print(list)

#example - 5

# list = [x for x in range(100) if x%3 == 0 if x%5 == 0]
# print(list)

#example - 6

# list = ["even" if x %2 == 0 else 'Odd' for x in range(100)]
# print(list)

#example - 7

# list = [(x,y) for x in [1,2,3,4,5,6] for y in [3,4,5,6,7,8,9]]
# print(list)

#dic comprehenension

#exm - 1
# dct = {i:i+10 for i in range(10)}
# print(dct)

#exam - 2
# dct = {'jack': 30,'rahim':23,'karim':21}
# new_dct = {k:v for k,v in dct.items() if v%2 == 0}
# print(new_dct)

#exam - 3
# dct = {'jack':30,'rahim':22,'karim':23}
# new_dct = {k:v for k,v in dct.items() if v%2 != 0 if v>18}
# print(new_dct)

#exam - 4

dct = {'jack':30,'rahim':22,'karim':23}
new_dct = {k:('old' if v >= 50 else 'young') for k, v in dct.items()}
print(new_dct)

#exam - 5

dcct = {k1:{k1*k2} for k2 in range (6) for k1 in range(5)}
print(dct)