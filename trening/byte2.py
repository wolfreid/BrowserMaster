def longest_consec(strarr, k):
    mini_list = []
    macro_list=[]
    result_text = ""
    if strarr and k>0 and k<len(strarr):
        for i in range(len(strarr)):
            for item in strarr[i:k+i]:
                mini_list.append(item)
            macro_list.append(mini_list)       
            mini_list = []
        for target_list in macro_list:
            current_text = "".join(target_list)
            if len(result_text) < len(current_text):
                result_text = current_text
    return result_text


# list1 = ['sdasdsad', 'asdasdasdasdasdasdasdas', 'asdasdasdasdasdasdasdasd', 'sdas', 'sd']
# print(sorted(list1))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))