import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from task12 import*

def extract_data_from_imdb(movie_url):
    res=requests.get(movie_url)
    return BeautifulSoup(res.text,"html.parser")

dictionary={}
def extract_language_from_imdb(imdb_data):
    for i in range(1):
        try:
            sum_data=imdb_data.find("div",class_="article",id="titleDetails")
            data=sum_data.find_all("div",class_="txt-block")
            Language_list=[]
            for index in data[:5]:
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
    dictionary["Languages"]=Language_list
    dictionary["country"]=country

def extract_director_from_imdb(imdb):
    bio_main_div=imdb.find("div",class_="plot_summary")
    bio_detail=bio_main_div.find("div",class_="summary_text").get_text().strip()

    director_detail=bio_main_div.find("div",class_="credit_summary_item")
    director_list=director_detail.findAll("a")
    director_new_list=[]  

    for dir in director_list:
        director_index=dir.get_text()
        director_new_list.append(director_index)
        
    dictionary["director"]=director_new_list
    dictionary["bio"]=bio_detail
    
def extract_movie_heading_from_imdb(imdb):
    heading_detail=imdb.find("div",class_="title_wrapper")
    movie_name=heading_detail.h1.get_text()
    name_split=movie_name.split()
    name=" ".join(name_split[:-1])

    movie_runtimes=imdb.find("div",class_="subtext").time["datetime"]
    time=" "     
    for i in movie_runtimes:
        if i.isdigit():
            time=time+i
    movie_runtime=int(time)

    j=imdb.find("div",class_="subtext").findAll("a")
    genre_list=[]
    for genre in j[:-1]:
        g=genre.get_text()
        genre_list.append(g)
    dictionary["genres"]=genre_list
    dictionary["name"]=name
    dictionary["runtime"]=movie_runtime

def Scrap_Movie_Detail(movie_url):
    soup = extract_data_from_imdb(movie_url)  

    languagesAndcountry=extract_language_from_imdb(soup)

    all_headings=extract_movie_heading_from_imdb(soup)

    data_dict=extract_director_from_imdb(soup)

    caste=part_of_movie_cast_url(movie_url)
    caste1=scrape_movie_cast(caste)

    dictionary["cast"]=caste1
    poster_url=soup.find("div",class_="poster").img["src"]
    dictionary["poster_image_url"]=poster_url
    return dictionary
movie_url1="https://www.imdb.com/title/tt0066763/"
particular_movie_detail=Scrap_Movie_Detail(movie_url1)
pprint(particular_movie_detail)
