from pprint import pprint
from Top_Indian_Movie_List import*
from movie_Url_detail import*



def Scrap_Movie_list_detail(movies):
        total_list=[]
        for movies_link in movies[:10]:
                particular_movie_url=movies_link["url"]
                particular_movie=Scrap_Movie_Detail(particular_movie_url)
                # pprint(particular_movie)
                total_list.append(particular_movie)
        pprint(total_list)
movie_list_detail1=(Scrap_Movie_list_detail(all_movies)) 
# pprint(movie_list_detail)