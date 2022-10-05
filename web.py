from bs4 import BeautifulSoup
import pandas as pd
import requests 

starDataurl='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
requestpage= requests.get(starDataurl)

soup= BeautifulSoup(requestpage.text,'html.parser')

starTable= soup.find('table')
templist=[]

tablerows= starTable.find_all('tr')

for i in tablerows: 
    tabledata= i.find_all('td')
    templist.append(tabledata)


starinfo=[]
distance=[]
mass=[]
radius=[]
luminous=[]

for i in range(1,len(templist)):
    starinfo.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    luminous.append(templist[i][7])

dataframe= pd.DataFrame(list(zip(starinfo,distance,mass,radius,luminous)),columns=['Star_Name','Distance','Mass','Radius','Luminousity'])
dataframe.to_csv('output.csv')





    