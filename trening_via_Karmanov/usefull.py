one_iterable = [2, 1, 3, 4, 7, 11]
# another_iterable = ['p', 'y', 't', 'h', 'o', 'p']
# for n, letter in zip(one_iterable, another_iterable):#для обработки нескольких массивов одновременно
#     print(letter, n)
# new_iter = set(another_iterable)
# print(new_iter)

# color_counts = [('red', 2), ('green', 1), ('blue', 3), ('purple', 5)]
# print(type(color_counts))
# for i in color_counts:
#     print(type(i))

# Синтаксис нарезки 
vars = []
for n in one_iterable[::-1]:
    vars.append(n)
    #  vars.extend(n)!Wrong    
print(vars)

# Метод переворота на месте
one_iterable.reverse()
for n in one_iterable:
    print(n)
print(one_iterable)