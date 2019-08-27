from task9 import*
from pprint import pprint

def get_genres_list(movies_list):
    genre_list=[]
    for index in movies_list:
        genres=index["genres"]
        genre_list.extend(genres)
    return genre_list
all_genres=get_genres_list(movie_list_detail)

def get_duplicate_genre(total_genres):
    genres=[]
    for genre in all_genres:
        if genre not in genres:
            genres.append(genre)
    return genres
genre_duplicate_list=get_duplicate_genre(all_genres)
# pprint(genre_duplicate_list)

genre_dict={}
def analyse_movies_genre(total_genre_list,dupicates_genre):
    for genres in dupicates_genre:
        count=0
        for particular_genre in total_genre_list:
            if genres==particular_genre:
                count=count+1
        genre_dict[genres]=count
    return genre_dict
genres_counting = analyse_movies_genre(all_genres,genre_duplicate_list)
pprint(genres_counting)