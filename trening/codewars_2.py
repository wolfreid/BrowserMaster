def solution(n):
    rome = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    for key in rome.keys():
        if n<= key:
            return key
    #     if n <10:
            
    #     elif n<100:
            
    #     elif n<1000:
            
    # if  to roman string
    # return
# x = 6
# add = lambda y: true if true else false 
# add = lambda y: sorted([i for i in range(y)],reverse=True)
# add2= lambda y: list(reversed(sorted([i for i in range(y)]))) if type(y) == int else y
# result = add(x)
# result.sort() 
# print("%s uses sort() and this one %s for uses sorted and this one %s uses list&reversed" %  (result,add(x),add2(x)))

# drinks = {
#      'martini': {'vodka', 'vermouth'},
#      'black russian': {'vodka', 'kahlua'},
#      'white russian': {'cream', 'kahlua', 'vodka'},
#      'manhattan': {'rye', 'vermouth', 'bitters'},
#      'screwdriver': {'orange juice', 'vodka'}
#      }
print(solution(10))