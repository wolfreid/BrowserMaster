def countBits(n):
    train_set = bin(n)
    newvalue = str(train_set)
    return newvalue.count("1")

print(countBits(1234))

####################################################################
def is_isogram(string):
    string = string.lower()
    temp = set(string)
    if len(string) == len(temp) and (string == " " or string.isspace() or string.isalpha()):
        return True
    else:
        return False
#######################################################################
array = [2, 4, 0, 100, 4, 11, 2602, 36]
        
def find_outlier(integers):
    count_even = 0
    count_odd = 0
    с = []
    for val in integers:
        if val % 2 == 0:
            count_even += integers.index(val) 
        else:
            count_odd += integers.index(val)
    c = sorted([count_even,count_odd])
    return  integers[c[0]]
##########################################################################
def nb_year(p0, percent, aug, p):
    total = p0
    year = 0
    while total <= p:
        total=total+total*(percent/100)+aug
        year+=1
    return year
##################################################################
def rgb(r, g, b):
    color_code = [r,g,b]
    result = []
    new_result=""
    translate_bit = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    for color in color_code:
        if color <=0:
            color = 0
        elif color > 255:
            color = 255 
        new_number =[color//16,color % 16]
        result +=new_number
    for val in result:
        if val > 9 :
            val=translate_bit[val]
        new_result +=str(val)
    return new_result
#############################################################################
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
##############################################################################
# print("ok",rgb(-20, 275, 125))
def sad():
    a = 5
    return "all" if a == 5 else 1
print(sad())