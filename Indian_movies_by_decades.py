from pprint import pprint
from Top_Indian_movies_by_year import years_data


sorted_year_list=years_data["sort_list"]
years_dict_data=years_data["years_group"]

def getDecades(group_of_years,movie_group_of_year):
    dictionary={}
    index=0
    while index<len(movie_group_of_year):
        years_list=[]
        get_modulus=movie_group_of_year[index]%10
        decade_year=movie_group_of_year[index]-get_modulus
        range_year=decade_year+10
        for j in range(decade_year,range_year):
            if j in movie_group_of_year:
                years_list.extend(group_of_years[j])
        dictionary[decade_year]=years_list
        index=index+1
    return dictionary
get_decades=getDecades(years_dict_data,sorted_year_list)
pprint(get_decades)