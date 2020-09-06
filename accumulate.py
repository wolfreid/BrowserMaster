a = [1,2,3,4,5]
b = [sum(a[:index]) for index,value in enumerate(a)]
print(b)