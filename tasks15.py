from task9 import movie_list_details
from pprint import pprint

def count_actors_act(movies_list,actor):
    count=0
    actor_dict={}
    for j in movies_list:
        actor_cast=j["cast"]
        for index in actor_cast:
            if index["name"]==actor:
                count=count+1
    if count>1:
        actor_dict["name"]=actor
        actor_dict["num_movies"]=count
        return actor_dict

def analyse_actors(movies_detail):         
    actors_dict={}
    for index in movies_detail[:20]:
        actors_name=index["cast"]
        for i in actors_name:
            actor_name=i["name"]
            data=count_actors_act(movies_detail,actor_name)
            if data == None:
                continue
            else:
                ids=i["imdb_id"]
                actors_dict[ids]=data
    pprint(actors_dict)
analyse_actors(movie_list_details)