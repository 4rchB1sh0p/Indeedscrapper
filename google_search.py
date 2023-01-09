# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:20:04 2023

@author: Dell
"""
import re
import pandas as pd
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
#fn to remove the brackets
def drop_brackets(town):
    town=re.sub("[\(\[].*?[\)\]]", "",town)
    return town
#the list of useless websites
def drop_webname(webz):
    drop_status = " "
    drop_web = ["baumaschinen", "facebook", "instagram", "ebay", "wikipedia", "maschinensucher", "gebrauchtmaschinen"]
    for i in range(len(drop_web)):
        if (webz.find(drop_web[i]) != -1):
            break
            drop_status = "remove"
        else:
            drop_status = "keep"
    return drop_status
search_result=[]
#Scrape from Wekipedia 
#tables=pd.read_html("https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Germany")
german_towns = pd.read_csv ('List_German_towns.csv')
print(german_towns['town'][2])
german_towns['town']=german_towns['town'].map(lambda x:drop_brackets(x))
# to search
#search.get("www.google.com", headers = {'User-agent': 'your bot 0.1'})
search_type = "Gebrauchtmaschinen"
for i in range(1,300,100):
    query= german_towns['town'][i]+search_type
    for j in search(query, tld="co.in", num=15, stop=15, pause=3):  
        search_result.append(j)
        print(j)
[ x for x in search_result if "ebay" not in x ]
websites=pd.DataFrame(search_result, columns =['name'])
websites['drop_status'] = websites['name'].map(lambda x:drop_webname(x))
indexAge = websites[(websites['name'].find("ebay") != -1)].index
websites.drop(indexAge , inplace=True)
websites.head(15)
websites.to_csv('gebrauchtwagen_websites.csv')