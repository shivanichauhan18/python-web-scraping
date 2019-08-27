from task9 import movie_list_detail
from pprint import pprint

def movies_director_list(movies_list):
    all_director_list=[]
    for index in movies_list:
        all_director_list.extend(index["director"])
    return all_director_list
director_list=movies_director_list(movie_list_detail)

def removing_duplicate_director(list):
    director_list=[]
    for i in list:
        if i not in director_list:
            director_list.append(i)
    return director_list
directors_list=removing_duplicate_director(director_list)
# pprint(directors_list)
def analyse_movies_directors(duplicate_director_list,total_directors_list):
    dictionary={}
    for main_dir in duplicate_director_list:
        count=0
        for campare_dir in total_directors_list:
            if main_dir == campare_dir:
                count=count+1
        dictionary[main_dir]=count
    pprint (dictionary)
# pprint(analyse_movies_directors(directors_list,director_list))