# text = "Python is an interpreted, high-level, general-purpose programming language"
text = input("make a sentence:")

def make_array(text):
    my_list = text.split()
    my_list.append("word")
    new_list = []
    for word in my_list:
        word = word.lower()
        new_list.append(word)
    return new_list

with open("file.txt", "w") as text_file:
    sentence = make_array(text)
    for line in sentence: 
        text_file.write(line+"\n")

x = input("Press ENTER to exit")

with open("file.txt", "a") as text_file:
    text_file.write("my new case")



