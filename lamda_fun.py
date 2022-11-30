# def greet():
#     print('Good Morning')

# greet()

# #lamda expression
# a = lambda : print("Good Morning")
# a()

#ex 1
# str = "Phitron"
# new_string = lambda string : string.upper()[::-1]

# print(new_string(str))

#ex 2
mx = lambda a,b : a if(a>b) else b
# print(mx(3,4))
print(mx(mx(6,5),mx(3,4)))

#ex 3
