def palendrom(text):
    seq = list()
    for iter, character  in enumerate(text):
        seq +=character
    qes=list(reversed(seq))
    if qes == seq:
        print("palindrom")
    else:
        print("not palindrom")



example = input()
palendrom(example)    