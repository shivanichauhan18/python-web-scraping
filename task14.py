from task9 import movie_list_details
from pprint import pprint

def get_Cast_list(movie_list):
    cast_nested_list=[]
    for i in movie_list:
        cast_nested_list.append(i["cast"][:5])
    return cast_nested_list
data_list=get_Cast_list(movie_list_details)
# pprint(data_list)

def get_lead_actor(nested_cast_list_data):
        lead_actors_list=[]
        for index in nested_cast_list_data:
                if index[0]["name"] not in lead_actors_list:
                        lead_actors_list.append(index[0]["name"])
        return lead_actors_list
lead_Actors_list=get_lead_actor(data_list)
# pprint (lead_Actors_list)

co_actors=[]
def lead_actor_dicts(lead_list):
        for i in lead_list:
                lead_Actors_Movies=[]
                for j in data_list:
                        if i in j[0]["name"]:
                                lead_Actors_Movies.append(j)
                co_actors.append(lead_Actors_Movies)
                # print("-----------------------------------")
        return co_actors
lead_co_actors=lead_actor_dicts(lead_Actors_list)
# pprint (lead_co_actors)

main_dict={}
for actors_info in lead_co_actors:
        Actor_dict={}
        main_lead_actor=actors_info[0][0]["name"] # THIS IS lead Actor hai
        main_lead_actor_id = actors_info[0][0]["imdb_id"]
        list1=[]
        co_actors_list=[]
        for i in actors_info:
                for j in i[1:]:
                        list1.append(j["name"])
                        if j not in co_actors_list:
                                co_actors_list.append(j)

        # Duplicates Nikale h list1 me se jisme hamne sare nested list k actors k name nikale the 
        actors=[]
        for b in list1:
                if b not in actors:
                        actors.append(b)

        frequent_co_actors=[]
        for k in actors:
                dict={}
                count=0
                for s in list1:
                        if k == s:
                                count=count+1
                if count>1:
                        for l in co_actors_list:
                                if l["name"]==k:
                                        if l["name"] not in l:
                                                l["no_movies"]=count
                                                frequent_co_actors.append(l)
        if frequent_co_actors != []:
                Actor_dict["name"]=main_lead_actor
                Actor_dict["frequent_co_actors"]=frequent_co_actors
                main_dict[main_lead_actor_id]=Actor_dict
pprint (main_dict)
























