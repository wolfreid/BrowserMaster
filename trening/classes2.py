genres = ["horror", "comedy", "drama", "action"]

library = {
    0 : ["default", "default"]
}

a = rand()
print(a)
while True:
    film = input("Enter film name: ")
    genre = input("Enter film genre: ")
    if genre in genres and film.isalpha():
        for item in library.values():
            if film in item:
                switch = 1
                break   
    if switch == 1: 
        current_genre_index = genres.index(genre)
        film_id = len(library) + 1
        library.update( { film_id : [film, genres[current_genre_index]] } )
        continue
    else:
        print ("This genre or film doesn't exist")
        break

print (library)

#####################################################################################

target_genre = input("What genre would you like to see? ")
for film_id in library:
    if target_genre in library[film_id]:
        print(library[film_id][0])

