classification =["id","name","genre"] 
genre =["horror","scifi","drama","comedy"] 
set_list = [(genre.index(i)+1,i) for i in genre]
genre_set =[] 
films = []
big_list =[]
while True:
    film = input()
    item_genre = input("wich genre? ")
    if item_genre in genre and film.isalpha():
        films.append(film)
        genre_set.append(genre.index(item_genre)+1)
        continue
    else:
        if not films:
            exit()       
        break

total = list(zip(genre_set, films)) 
for genre_prop in set_list:
    for n,film in enumerate(total):
        if film[0] == genre_prop[0]:
            block = {classification[0]:n,classification[1]:film[1],classification[2]:genre_prop[1]}
            big_list.append(block)
        

text = " "
whats_next = input("whats_next ")
if whats_next == "names":
    for block in big_list:
        text+=block['name']
    print(text,len(big_list))
    text = " "   
elif whats_next == "genres":
    for block in big_list:
        text+=block["genre"]
    print(text,"",big_list())
    text = " "
elif whats_next == "all":
   pass
# print(films)
# print(set_list)
# print(genre_set)

# print(total[1])