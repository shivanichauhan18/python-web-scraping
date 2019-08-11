import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

def Scrap_Movie_Detail(movie_url):
    dictionary={}
    res=requests.get(movie_url)
    soup=BeautifulSoup(res.text,"html.parser")

    bio_main_div=soup.find("div",class_="plot_summary")
    bio_detail=bio_main_div.find("div",class_="summary_text").get_text().strip()

    poster_div=soup.find("div",class_="poster")
    poster_url=poster_div.img["src"]



    director_detail=bio_main_div.find("div",class_="credit_summary_item")
    director_list=director_detail.findAll("a")
    director_new_list=[]
    for dir in director_list:
        director_index=dir.get_text()
        director_new_list.append(director_index)
    # print director_new_list



    heading_detail=soup.find("div",class_="title_wrapper")
    movie_name=heading_detail.h1.get_text()


    movie_runtime=heading_detail.find("div",class_="subtext")
    runtime=movie_runtime.time["datetime"]                  

    movie_genre=heading_detail.find("div",class_="subtext")
    j=movie_genre.findAll("a")
    k=0
    genre_list=[]
    while (k<(len(j))-1):
        g=j[k].get_text()
        genre_list.append(g)
        k=k+1
    # print genre_list
    try:
        sum_data=soup.find("div",class_="article",id="titleDetails")
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
        print ("------------")

    
    dictionary["Country"]=country
    dictionary["name"]=movie_name
    dictionary["genre"]=genre_list
    movie_run=runtime[2:5]
    dictionary["runtime"]=int(movie_run)
    dictionary["bio"]=bio_detail
    dictionary["poster_image_url"]=poster_url
    dictionary["director"]=director_new_list
    dictionary["Language"]=Language_list
    pprint(dictionary)
movie_url="https://www.imdb.com/title/tt0066763/"
pprint(Scrap_Movie_Detail(movie_url))