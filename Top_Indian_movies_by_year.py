from pprint import pprint
from Top_Indian_Movie_List import*

def getMovieYearList(total_movies):
    i=0
    new_list=[]
    while i<len(total_movies):
        movie_year=total_movies[i]["year"]
        if movie_year not in new_list:
            new_list.append(movie_year)
        i=i+1
    return new_list
get_movie_list=getMovieYearList(all_movies)

def group_by_year(movies,new_list2):
    j=0                          # for i in range (decade_year,range_year)
    year_dict={}
    while j<len(new_list2):
        particular_year_list=[]
        index=new_list2[j]
        for dict_data in  movies:
            if index == dict_data["year"]:
                particular_year_list.append(dict_data)
        year_dict[index]=particular_year_list
        j=j+1
    return year_dict
year_dict=group_by_year(all_movies,get_movie_list)
pprint(year_dict)

def data_list(sorted_list,group_of_year):
    dict={}
    dict["sort_list"]=sorted_list
    dict["years_group"]=group_of_year
    return dict
years_data=data_list(get_movie_list,year_dict)
# pprint(years_data)