import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

url="https://www.imdb.com/india/top-rated-indian-movies/"
def getTopMoviesList(url):
    movie_dict={}
    requests_data=requests.get(url)
    soup=BeautifulSoup(requests_data.text,"html.parser")
    tbody=soup.find("tbody",class_="lister-list")
    trs=tbody.findAll("tr")

    year_list=[]
    ratting_list=[]
    url_list=[]
    name_list=[]
  
    for tr in trs:
        name = tr.find("td",class_="titleColumn").a.get_text()
        name_list.append(name)

        movie_url=tr.find("td",class_="titleColumn").a["href"]
        movies_link="https://www.imdb.com"+movie_url
        url_list.append(movies_link)

        movie_year=tr.find("td",class_= "titleColumn").span.get_text()
    tbody=soup.find("tbody",class_="lister-list")
    trs=tbody.findAll("tr")

    year_list=[]
    ratting_list=[]
    url_list=[]
    name_list=[]
  
    for tr in trs:
        name = tr.find("td",class_="titleColumn").a.get_text()
        name_list.append(name)

        movie_url=tr.find("td",class_="titleColumn").a["href"]
        movies_link="https://www.imdb.com"+movie_url
        url_list.append(movies_link)

        movie_year=tr.find("td",class_= "titleColumn").span.get_text()
        year_list.append(movie_year)

        movie_ratting=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        ratting_list.append(movie_ratting)
        
    movies_list=[]
    years_list=[]
    for i in range(0,250):
        dict={}
        dict["rating"]=float(ratting_list[i])
        dict["position"]=i+1
        dict["name"]=name_list[i]
        dict["url"]=url_list[i]
        dict["year"]=int(year_list[i][1:5])
        years=dict["year"]
        year_list.append(years)
        movies_list.append(dict)
    return movies_list
all_movies=getTopMoviesList(url="https://www.imdb.com/india/top-rated-indian-movies/")


def Scrap_Movie_Detail(movie_url):
    for movies_links in movie_url:
        movies_url=movies_links["url"]
        # print movies_url
        dictionary={}
        res=requests.get(movies_url)
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
        dictionary["runtime"]=movie_run)
        dictionary["bio"]=bio_detail
        dictionary["poster_image_url"]=poster_url
        dictionary["director"]=director_new_list
        dictionary["Language"]=Language_list
        pprint(dictionary)

pprint(Scrap_Movie_Detail(all_movies))

# super-30 movie link -----https://www.uwatchfree.st/2019/07/super-30-2019-full-movie/