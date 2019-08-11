import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from Top_Indian_Movie_List import getTopMoviesList

def getMovieYear(total_movies):
    i=0
    new_list=[]
    while i<len(total_movies):
        movie_year=total_movies[i]["year"]
        new_list.append(movie_year)
        i=i+1
    new_list.sort()

    new_list2=[]
    for i in new_list:
        if i not in new_list2:
            new_list2.append(i)
    return new_list2
url="https://www.imdb.com/india/top-rated-indian-movies/"
h=getTopMoviesList(url)
get_movie_list=getMovieYear(h)
# print get_movie_list

# pprint(all_movies) 

url="https://www.imdb.com/india/top-rated-indian-movies/"

def group_by_year(movies,new_list2):
    j=0        # for i in range (decade_year,range_year)

    year_dict={}
    while j<len(new_list2):
        particular_year_list=[]
        index=new_list2[j]
        for dict_data in  h:
            if index == dict_data["year"]:
                particular_year_list.append(dict_data)
        year_dict[index]=particular_year_list
        j=j+1
    return year_dict
year_dict=group_by_year(h,get_movie_list)
pprint(year_dict)