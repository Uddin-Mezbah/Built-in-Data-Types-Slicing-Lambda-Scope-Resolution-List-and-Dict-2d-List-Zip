#namespace scope

# x=5
# x=3
# y=10

# def f():
#     print("")
# import numpy as np
# np.f()

# LEGB
# L = locals
# E = Enclosed(nested function)
# G = global
# B = Builtin

#local global
# s = "I am global"

# def f():
#     s = "I am local"
#     print(s)

# f()
# print(s)

#enclosed scope

# s = "i am global"
# def outer_scope():
#     s = "I am local"
#     def inner_scope():
#         s = "I am enclosed"
#         print(s)
#     inner_scope()
# outer_scope()

#built in 
from math import pi
print(pi)
s = "I am global"
pi = 34.11

def outer_scope():
    pi = 33.11
    def inner_scope():
        pi = 33.11
        print(pi)

    inner_scope()
outer_scope()
