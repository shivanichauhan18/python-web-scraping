import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import os.path

def part_of_movie_cast_url(urls):
        url_list=[]
        requests_data=requests.get(urls)
        soup=BeautifulSoup(requests_data.text,"html.parser")
        casting=soup.find("div",class_="article",id="titleCast")
        url_part=casting.find("div",class_="see-more").a["href"]
        url1=urls+url_part
        return url1
cast_url=part_of_movie_cast_url("https://www.imdb.com/title/tt0066763/")


def writting_data(fileName,scrap_data):
    with open (fileName,"w") as files:
        dumps_file=json.dumps(scrap_data)
        files.write(dumps_file)

def read_scrap_data(fileName):
    with open (fileName,"r") as Rdata:
        read_data=Rdata.read()
        load_data=json.loads(read_data)
    return load_data


def scrape_movie_cast(cast_url_list):        
        id=cast_url_list.split("/")
        movie_id=id[4] 
        fileName="caste_details/"+movie_id+"_cast.json"

        if os.path.exists(fileName):
                h=read_scrap_data(fileName)
                return h
                print("file is reading")
        else:
                requests_data=requests.get(cast_url_list)
                soup=BeautifulSoup(requests_data.text,"html.parser")
                main_table_div=soup.find("table",class_="cast_list")
                trs=main_table_div.findAll("tr")
        
                Actors_id_and_name=[]
                for i in trs[1:]:
                        dict={}
                        # Id of Actor/Actorees
                        try:
                                tds= i.find_all("td")
                                href=tds[1].a["href"]
                                get_id=href.split("/")
                                id=get_id[2]

                                # Name of Actor/Actorees
                                Name=tds[1].get_text().strip()

                                dict["imdb_id"]=id
                                dict["name"]=Name

                                Actors_id_and_name.append(dict)
                        except IndexError:
                                continue                               
                writting_data(fileName,Actors_id_and_name)
                print("file is writing")
caste=scrape_movie_cast(cast_url)
# pprint(caste)