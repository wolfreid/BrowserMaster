import numpy as np
def get_pins(observed):
    len_observed = len(list(str(observed)))
    keybord = np.array([['1','2','3'],['4','5','6'],['7','8','9'],['','0','']])
    rows=keybord.shape[0]
    columns=keybord.shape[1]
    result=[0] * len_observed
    for step,i in enumerate(list(str(observed))):
        for row in range(rows):
            for column in range(columns):
                if keybord[row,column] == i:
                    back = 0 if column== 0 else 1
                    jump = 0 if column == 2 else 1
                    up = 1 if row == 3 else 2
                    down =0 if row == 0 else row-1
                    close_arr =[np.take(keybord[n],range(column-back,column+1+jump)) for n in range(down,row+up)]
        my_set =[(row,column) for row,sublist in enumerate(close_arr) for column, character in enumerate(sublist)\
             if character == i] 
        result[step]  = [x for (row,column),x in np.ndenumerate(close_arr) if (int(row)==my_set[0][0] or int(column)==my_set[0][1])\
                            and x != ""]
    result = list(map(lambda x:"".join(x),result))
    list_properties =list(map(lambda x:len(x),result))
    list_accumulate = [0]+[sum(list_properties[:verge+1]) for verge in range(len(list_properties))]    
    new_result = ["".join(line) for line in permutations("".join(result),len_observed,list_accumulate) if len(line) == len_observed]
    if len_observed==1:
        new_result.insert(0,result[0][0])
    return new_result

def permutations(iterable, r=None,a=[]):
    pool = tuple(iterable)
    n = len(pool)
    indices = list(range(n))
    cycles = list(range(n, n-r,-1))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i] 
                yield tuple(pool[i] for index,i in enumerate(indices[:r]) if i in\
                     (lambda temp:range(temp[0],temp[1]))(temp =a[index:]))
                break
        else:
            return


print(get_pins('369'))
