#labda function
lresult=lambda a,b:a+b
print(lresult(20,3))

biggest=lambda a,b:a if a>b else b
print(biggest(10,20))

#filter
def isEven(a):
    if a%2==0:
        return true
    else:
        return false

mylist=[1,2,3,4,5,6]
r=list(filter(isEven,mylist))
print(r)


#map function
mylist=[1,2,3,4,5,6]
def doubleme(a):
    return a*2

list1=list(map(doubleme,mylist))
print(list1)

#can be done with labda func
list1=list(map(lambda x:2*x,mylist))
print(list1)

l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

from functools import *
mylist=[1,2,3,4,5]
r=reduce(lambda a,b:a+b,mylist)
print(r)


#webscraping
import requests
try:
    s=requests.get("https://www.imdb.com/chart/top")
    stats=s.raise_for_status()
    print(stats)

except Exception as e:
    print(e)

#using the library-->beautiful soap
import requests
from bs4 import BeautifulSoup
try:
    s = requests.get("https://www.imdb.com/chart/top")
    soup=BeautifulSoup(source.text,'html.parser')
    movies=soup.find('tbody', class_="lister-list").find_all('tr')

except Exception as e:
    print(e)



f=open("imdb.txt",'a')
for movie in movies:
    rank=movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
    print(rank)
    name=movie.find('td',class_='titleColumn').a.text
    print(name)
    year = movie.find('td', class_='titleColumn').span.text.strip('()')
    print(year)
    rating= movie.find('td', class_='titleColumn').strong.text
    print(rating)

    print(rank,name,year,rating)


    f.write(rank)
    f.write(" ")
    f.write(name)
    f.write(" ")
    f.write(year)
    f.write(" ")
    f.write(rating)


list1=[[1,2,3,4],[5,6,7,8],[1,3,5,8]]
print(lis1)
print(len(list1))
for nos in list1:
    print(nos)


    #checkdebugging



