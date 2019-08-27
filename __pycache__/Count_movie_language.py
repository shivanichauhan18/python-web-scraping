from Top_Movie_List_Url_Detail import*

def movies_all_language_list(all_novies_list):
        new_language_list=[]
        for j in all_novies_list:
                new_language_list.extend(j["Language"])
        return new_language_list
all_languages=movies_all_language_list(movie_list_detail)


def get_main_language_list(list):
        removing_duplicate_list=[]
        for i in list:
                if i not in removing_duplicate_list:
                        removing_duplicate_list.append(i)
        return removing_duplicate_list
duplicate_list=get_main_language_list(all_languages)


def analyse_movies_language(Language_list,list):
        dictionary={}
        for Language in Language_list:
                count_language=0
                for particular_language in list:
                        if Language == particular_language:
                                count_language=count_language+1
                dictionary[Language]=count_language
        return dictionary
movie_list_languages=analyse_movies_language(duplicate_list,all_languages)
pprint(movie_list_languages)
