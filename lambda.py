people = [
    {"name":"Masoud","house":"Yazdanmehr"},
    {"name":"Peyman","house":"Chogiah"},
    {"name":"Mohsen","house":"Delgosha"},
    {"name":"Javid","house":"Fazilat"},
]

#def f(parm):
    #return parm["name"]
#    return parm["house"]
#people.sort(key=f)

people.sort(key=lambda parm:parm['name'])
print(people)
people.sort(key=lambda parm:parm['house'])
print(people)