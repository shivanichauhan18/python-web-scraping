from Count_movie_director import*
from task9 import*
dict={}

for index in directors_list:
        language_list=[]
        for j in movie_list_detail:
                if index in j["director"]:
                        language_list.extend(j["Languages"])

# this program for dublicate 
        new_language_list=[]
        for language in language_list:
                if language not in new_language_list:
                        new_language_list.append(language)

#this program for counting language
        dictionary={}
        for particular_language in new_language_list:
                count=0
                for i in language_list:
                        if particular_language == i:
                                count=count+1
                dictionary[particular_language]=count

        dict[index]=dictionary
pprint(dict)
        
                
        
                
   
