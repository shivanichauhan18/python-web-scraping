import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint



def extract_data_from_imdb(movie_url):
    res=requests.get(movie_url)
    return BeautifulSoup(res.text),"html.parser"


def extract_language_from_imdb(imdb_data):
    for i in range(1):
        dict={}
        try:
            sum_data=imdb_data.find("div",class_="article",id="titleDetails")
            data=sum_data.find_all("div",class_="txt-block")
            Language_list=[]
            for index in data:
                h4_data=index.find("h4",class_="inline").get_text()
                if h4_data == "Language:":
                    data1=index.findAll("a")
                    for i in data1:
                        lANGUAGES=i.get_text()
                        Language_list.append(lANGUAGES)
                if h4_data == "Country:":
                    country=index.a.get_text()
        except AttributeError: 
            continue
    dict["Languages"]=Language_list
    dict["country"]=country
    return dict


def extract_director_from_imdb(imdb):
    dir_and_bio_dict={}
    bio_main_div=imdb.find("div",class_="plot_summary")
    bio_detail=bio_main_div.find("div",class_="summary_text").get_text().strip()

    director_detail=bio_main_div.find("div",class_="credit_summary_item")
    director_list=director_detail.findAll("a")
    director_new_list=[]    # dictionary={}

    for dir in director_list:
        director_index=dir.get_text()
        director_new_list.append(director_index)
        
    dir_and_bio_dict["director"]=director_new_list
    dir_and_bio_dict["bio"]=bio_detail
    return dir_and_bio_dict
    

def extract_movie_heading_from_imdb(imdb):
    dictionary={}
    heading_detail=imdb.find("div",class_="title_wrapper")
    movie_name=heading_detail.h1.get_text()
    name_split=movie_name.split()
    # name=" ".join(name_split[:-1])
    print name_split


#     movie_runtimes=heading_detail.find("div",class_="subtext")
#     runtime=movie_runtimes.time["datetime"]  
#     time=" "     
#     for i in runtime:
#         if i.isdigit():
#             time=time+i
#     movie_runtime=int(time)

#     j=movie_runtimes.findAll("a")
#     genre_list=[]
#     for genre in j[:-1]:
#         g=genre.get_text()
#         genre_list.append(g)

#     dictionary["genres"]=genre_list
#     dictionary["name"]=name
#     dictionary["runtime"]=movie_runtime
    print name_split



#     return dictionary

# def Scrap_Movie_Detail(movie_url):
#     soup = extract_data_from_imdb(movie_url)  

#     languagesAndcountry=extract_language_from_imdb(soup)

    all_headings=extract_movie_heading_from_imdb(soup)

#     data_dict=extract_director_from_imdb(soup)

#     poster_div=soup.find("div",class_="poster")
#     poster_url=poster_div.img["src"]

#     dictionary={}
#     dictionary["Country"]=languagesAndcountry["country"]
#     dictionary["name"]=all_headings["name"]
#     dictionary["genre"]=all_headings["genres"]
#     dictionary["runtime"]=all_headings["runtime"]
#     dictionary["bio"]=data_dict["bio"]
#     dictionary["poster_image_url"]=poster_url
#     dictionary["director"]=data_dict["director"]
#     dictionary["Language"]=languagesAndcountry["Languages"]
#     return dictionary
movie_url="https://www.imdb.com/title/tt0066763/"
particular_movie_detail=Scrap_Movie_Detail(movie_url)
pprint(particular_movie_detail)
