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
        year_list.append(movie_year)

        movie_ratting=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        ratting_list.append(movie_ratting)
        
    movies_list=[]
    dict={}
    for i in range(0,250):
        dict["rating"]=float(ratting_list[i])
        dict["position"]=i+1
        dict["name"]=name_list[i]
        dict["url"]=url_list[i]
        dict["year"]=int(year_list[i][1:5])
        movies_list.append(dict)
    return movies_list
all_movies=getTopMoviesList(url="https://www.imdb.com/india/top-rated-indian-movies/")
pprint(all_movies)

movies_dict={}
a=movies_dict["movies"]=all_movies
with open ("TopIndianMovies.json","w") as file:
    file_data=json.dumps(a)
    file.write(file_data)
