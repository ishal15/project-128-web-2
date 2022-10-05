from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url= 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page= requests.get(url)
soup= bs(page.text,'html.parser')
starTable= soup.find_all('table')
tablerows= starTable[7].find_all('tr')

list1=[]

for i in tablerows:
    tabledata= i.find_all('td')
    strip= [strip1.text.rstrip() for strip1 in tabledata]
    list1.append(tabledata)

starname=[]
raduis=[]
distance=[]
mass=[]

for i in range(1,len(list1)):
    starname.append(list1[i][0])
    raduis.append(list1[i][3])
    distance.append(list1[i][1])
    mass.append(list1[i][2])

datastore= pd.DataFrame(list(zip(starname,raduis,distance,mass)), columns=['star_name','radius','distance','mass'])
datastore.to_csv('project128output.csv')