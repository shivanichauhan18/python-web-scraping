import os.path
from pprint import pprint
from Top_Indian_Movie_List import*
from movie_Url_detail import*

def writting_data(fileName,scrap_data):
    with open (fileName,"w") as files:
        dumps_file=json.dumps(scrap_data)
        files.write(dumps_file)

def read_scrap_data(fileName):
    with open (fileName,"r") as Rdata:
        read_data=Rdata.read()
        load_data=json.loads(read_data)
    return load_data


def movieCashing(movies):
    count=0
    for particular_movies in movies[:10]:
        movie_url=particular_movies["url"]
        spliting=movie_url.split("/")
        get_id=spliting[4]
        id="movies_detail/"+get_id+"_caste.json"

        if os.path.exists(id):
            reading=read_scrap_data(id)
            pprint(reading)
        else:
            get_movie_detail=Scrap_Movie_Detail(movie_url)
            print "creting data%%%%%$$$$$$$$$$$$$$"
            file_writting=writting_data(id,get_movie_detail)
# function calling
movieCashing(all_movies)