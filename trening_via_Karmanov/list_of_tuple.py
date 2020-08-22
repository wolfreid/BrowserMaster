def palendrom(text):
    seq = []
    for character  in enumerate(text):
       seq.append(character) 
    print(seq)
    print(seq[1])
    print(seq[1][1])
    seq[0],seq[1] = seq[1],seq[0]
    print(seq) 

example = input()
palendrom(example)    