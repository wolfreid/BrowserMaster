x= {}
x.update({'var':1})
# print(x.items(), x.keys())
# print(x['var'])
x.update({'sar':2})
y = [5,6,7]
x.update({'dar':y})
# print(x)

y = {'y':5}


new_dict = x.copy()
new_dict.update({'jar':1})
# print(new_dict)
# print(new_dict.values())

del new_dict["jar"]
del y

new_dict.clear()
print(new_dict)

# i =0
# a = {}
# for name1  in zip(new_dict,x):
#     a[i] = set(name1)
#     i+=1
# print(a)    

