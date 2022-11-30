# nums = [1,2,3]
# string = ["one ",'two','three']
# new_obj = zip(nums,string)
# # print(list(new_obj))

# num = [1.1,2.2,3.3]
# new_obj=zip(nums,string,num)
# # print(set(new_obj))
# print(list(new_obj))

# nums = (1,2,3)
# string = ["one ",'two','three']
# new_obj = zip(nums,string)
# # print(list(new_obj))

# num = {1.1,2.2,3.3}
# new_obj=zip(nums,string,num)
# # print(set(new_obj))
# print(list(new_obj))

names = ['rahim','karim','halim']
salaries = [1000,30000,4000]
result = list(zip(names,salaries))
# print(list(zip(salaries,names)))

# new_db = {name:salary for name ,salary in zip(names,salaries)}
# print(new_db['rahim'])

name,salary = zip(*result)
print(name)
print(salary)

