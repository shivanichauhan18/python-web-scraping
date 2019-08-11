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
print len(all_movies)
# pprint(all_movies)


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
get_movie_list=getMovieYear(all_movies)
# print get_movie_list

def group_by_year(movies,new_list2):
    j=0        # for i in range (decade_year,range_year)

    year_dict={}
    while j<len(new_list2):
        particular_year_list=[]
        index=new_list2[j]
        for dict_data in  all_movies:
            if index == dict_data["year"]:
                particular_year_list.append(dict_data)
        year_dict[index]=particular_year_list
        j=j+1
    return year_dict
year_dict=group_by_year(all_movies,get_movie_list)
# pprint(year_dict)



def getDecades(year_group,movie_year_group):
    dictionary={}
    index=0
    while index<len(movie_year_group):
        new_list_a=[]
        get_modulus=movie_year_group[index]%10
        decade_year=movie_year_group[index]-get_modulus
        range_year=decade_year+10
        for j in range(decade_year,range_year):
            if j in movie_year_group:
                new_list_a.extend(year_group[j])
        dictionary[decade_year]=new_list_a
        index=index+1
    return dictionary
get_decades=getDecades(year_dict,get_movie_list)
pprint(get_decades)
        


# print new_list2[i]
        # if new_list2[i] in dictionary:
        #    dictionary[decade_year]=
        #if(new_list[i]['year'])
        # while new_list2[j]<range_year:
        #     k=new_list2[j]
        #     list1.extend(year_dict[k])
        #     # print j
        #     j=j+1
        # dictionary[decade_year]=list1
        # pprint(list1)
    # return dictionary





























# def group_by_decade(decade_year):
#     index=0  
#     dictionary={}
#     year=1960
#     k=0
#     while index<len(decade_year):
#         j=k
#         decade_list=[]
#         while j<len(new_list2):
#             if new_list2[j]<year :              #and new_list2[k]<year:
#                 decade_list.extend(year_dict[new_list2[j]])
#             else:               
#                 break
#             j=j+1
#         h=decade_year[index]
#         dictionary[h]=decade_list
#         index=index+1
#         k=j
#         year=year+10
#     return dictionary    
# dacade_year_data=group_by_decade([1950,1960,1970,1980,1990,2000,2010])
# pprint(dacade_year_data)
