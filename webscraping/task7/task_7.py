import json

file=open("task_5.json",'r')
dic=json.load(file)
file.close()

def analyse_movies_language(dc):
    s=set()
    dc=dc.values()
    for i in dc:
        ii=i["Director"]
        for j in ii:
            s.add(j)
    mov={}
    for j in s:
        ll=0
        for i in dc:
            ii=i["Director"]
            if j in ii:
                ll+=1
        mov[j]=ll
    print(json.dumps(mov,indent=4))
    file=open("task7.json","w")
    json.dump(mov,file,indent=4)
    file.close()
analyse_movies_language(dic)
