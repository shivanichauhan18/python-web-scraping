from pprint import pprint
from Top_Indian_Movie_List import*
from movie_Url_detail import*
import random
import time
import os.path

def writting_data(fileName,scrap_data):
    with open (fileName,"w") as files:
        dumps_file=json.dumps(scrap_data)
        files.write(dumps_file)

def read_scrap_data(fileName):
    with open (fileName,"r") as Rdata:
        read_data=Rdata.read()
        load_data=json.loads(read_data)
    return load_data

def Scrap_Movie_list_detail(movies):
    count=0
    total_movie_list=[]
    for movies_link in movies:
        particular_movie_url=movies_link["url"]
        spliting=particular_movie_url.split("/")
        get_id=spliting[4]
        id="movies_detail_data/"+get_id+".json"

        if os.path.exists(id):
            count=count+1
            reading=read_scrap_data(id)
            total_movie_list.append(reading)
        else:
            # print ("creting data%%%%%$$$$$$$$$$$$$$")
            particular_movie_detail=Scrap_Movie_Detail(particular_movie_url)
            
            file_writting=writting_data(id,particular_movie_detail)
            random_num=random.randint(1,3)
            time.sleep(random_num)
    return total_movie_list
        
movie_list_details=(Scrap_Movie_list_detail(all_movies)) 
# pprint(movie_list_details)