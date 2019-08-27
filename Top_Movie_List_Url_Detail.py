from pprint import pprint
from Top_Indian_Movie_List import*
from movie_Url_detail import*
import random
import time

def Scrap_Movie_list_detail(movies):
        total_list=[]
        for movies_link in movies[:10]:
                particular_movie_url=movies_link["url"]
                particular_movie_detail=Scrap_Movie_Detail(particular_movie_url)
                total_list.append(particular_movie_detail)
        return total_list
movie_list_detail=(Scrap_Movie_list_detail(all_movies)) 
pprint(movie_list_detail)