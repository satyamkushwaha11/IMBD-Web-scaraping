
# from typing import Text
import requests
import json
from bs4 import BeautifulSoup
url='https://www.imdb.com/india/top-rated-indian-movies/'
res=requests.get(url) 
soup = BeautifulSoup(res.text,"html.parser")


def scrape_top_list():    #task 1
    aa=soup.find("div",class_="lister")
    rr=aa.find("tbody",class_="lister-list")
    tr=rr.find_all("tr")
    allmovies={}
    # global movielist
    movielist=[]
    for i in tr:
        ddd=["Movie","Year","Position","Rating","Link"]
        detail=i.find("td",class_="titleColumn").text.strip().split("\n") #list of movie,year position
        detail.insert(1,(detail.pop(1)).strip())
        
        detail.insert(2,(detail.pop(2)).strip(')('))
        
        detail.insert(2,(detail.pop(0)).strip("."))
        
        detail.append(i.find("strong").string) # imbd rating
        
        detail.append('https://www.imdb.com'+str(i.find("td",class_="titleColumn").a['href'])) #for adding  link
        data=dict(zip(ddd,detail))
        
        movielist.append(data)
        

    allmovies.update({'Data':movielist})
    file=open("topmovies.json","w")
    json.dump(allmovies,file,indent=4)
    file.close()
    return movielist

movie=scrape_top_list()


# def group_by_year(mov):    #task 2
#     di={}
#     s=set()
#     for i in mov:
#         s.add(int(i['Year']))
    
#     for j in s:
#         l=[]
#         for k in mov:
#             if str(j)==k["Year"]:
#                 l.append(k)
#         di[j]=l

#     ff=open('group_by_year.json',"w")
#     json.dump(di,ff,indent=4) 
#     ff.close()
#     return di
        
# # group_by_year(movie)

# # gby=group_by_year(movie)


# def group_by_decade(l):     #task3
#     did={}
#     ss=set()
#     for i in l:
#         ss.add(i//10)
        
#     for j in ss:
#         ll=[]
#         for k in l:
#             if str(j) in str(k):
#                 for  a in l[k]:
#                     ll.append(a)
                    
                
#         did[f'{j}0']=ll
        
#     ff=open('group_by_decede.json',"w")
#     json.dump(did,ff,indent=4) 
#     ff.close()    

# # group_by_decade(gby)
