#!/usr/bin/env python
# coding: utf-8

# # Q1 Write a python program to display all the header tags from wikipedia.org

# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[6]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[7]:


page


# In[396]:


soup=BeautifulSoup(page.content)
soup


# In[397]:


soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[418]:


title = soup.find_all(['h1','h2','h3','h4','h5','h6'])

title


print('List all the header tags',*title,sep='\n\n')


# # Q2 Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame

# In[324]:


page = requests.get('https://www.imdb.com/chart/top/')


# In[325]:


page


# In[326]:


soup = BeautifulSoup(page.content)
soup


# In[327]:


soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[328]:


scraped_movies = soup.find_all('td',class_="titleColumn")
scraped_movies


# In[337]:


movies = []
for i in scraped_movies:
    i=i.get_text().replace('\n', "")
    i=i.strip(" ")
    movies.append(i)
movies[:100]


# In[331]:


scraped_ratings = soup.find_all('td',class_="ratingColumn imdbRating")
scraped_ratings


# In[336]:


ratings = []

for i in scraped_ratings:
    i=i.get_text().replace('\n', '')
    ratings.append(i)
ratings[:100]


# In[335]:


years=[]

for i in soup.find_all('span',class_="secondaryInfo"):
    years.append(i.text)
    
years[:100]


# In[334]:


df=pd.DataFrame({'Movies_Name':movies,'Year of release':years,'Ratings':ratings})
df.head(100)


# In[338]:


df.to_csv('IMDb Top Movies.csv',index=False)


# # Q3 Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame

# In[352]:


page = requests.get ('https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=XGK4CBYTX1A3R58DKHST&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_sm')


# In[353]:


page


# In[354]:


soup = BeautifulSoup(page.content,)
soup


# In[355]:


soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[367]:


name = []

for i in soup.find_all('td',class_="titleColumn"):
    i=i.get_text().replace('\n',"")
    i=i.strip(" ")
    name.append(i)
    
name[:100]


# In[361]:


year=[]

for i in soup.find_all('span',class_="secondaryInfo"):
    year.append(i.text)
    
year


# In[366]:


ratings = []

for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    i=i.get_text().replace('\n',' ')
    ratings.append(i)

ratings[:100]


# In[368]:


df=pd.DataFrame({'Movies_Name':name,'years of release': year,'Ratings':ratings})


# In[369]:


df.head(100)


# # Q4 Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)
# from https://presidentofindia.nic.in/former-presidents.htm

# In[370]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[371]:


page


# In[372]:


soup = BeautifulSoup(page.content)
soup


# In[ ]:


soup = BeautifulSoup(page.content)
soup


# In[373]:


soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[377]:


presidents_name = soup.find_all('div',class_="presidentListing")
presidents_name 


# In[384]:


name = []
for i in presidents_name :
    i=i.get_text().replace('\n', "")
    i=i.strip(" ")
    name.append(i)
name[:100]


# In[388]:


df=pd.DataFrame({'List of presidents of india (name,Term of office)':name})


# In[389]:


df


# In[390]:


df.to_csv('presedent of india.csv')


# In[391]:


df


# # Q5 Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# In[497]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[498]:


soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[478]:


scraped_team = soup.find_all('span',class_="u-hide-phablet")
scraped_team


# In[479]:


team = []
for i in scraped_team :
    i=i.get_text().replace('\n', "")
    i=i.strip(" ")
    team.append(i)
team[:10]


# # Q7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :

# In[508]:


page = requests.get('https://www.cnbc.com/world/?region=world')

page


# In[510]:


soup = BeautifulSoup(page.content,'html.parser')

print(soup.prettify())


# In[591]:


scraped_headline = soup.find_all('a',class_="LatestNews-headline")
scraped_headline


# In[592]:


headline = []

for i in scraped_headline:
    i=i.get_text().replace('\n', "")
    i=i.strip(" ")
    headline.append(i)
headline
    
    


# In[593]:


scraped_time = soup.find_all('time',class_="LatestNews-timestamp")
scraped_time


# In[594]:


time = []

for i in scraped_time:
    i=i.get_text().replace('\n', "")
    i=i.strip(" ")
    time.append(i)
time
    


# In[595]:


link = []

for i in soup.find_all('a',class_="LatestNews-headline"):
    link.append(i.get('href'))
link


# In[599]:


print(len(headline),len(time),len(link))


# In[601]:


df = pd.DataFrame({'Headline':headline,'Time':time,'News link':link})


# In[602]:


df


# In[603]:


df.to_csv('news details.csv')


# In[604]:


df


# # Q8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles

# In[619]:


page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')

page


# In[620]:


Soup = BeautifulSoup(page.content)

soup


# In[622]:


soup = BeautifulSoup(page.content,'html.parser')

print(soup.prettify())


# In[629]:


title = soup.find_all('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR")


# In[630]:


title


# In[633]:


Paper_title = []

for i in title:
    i=i.get_text().replace('\n', "")
    i=i.strip(" ")
    Paper_title.append(i)
Paper_title


# In[635]:


Authors = Soup.find_all('span',class_="sc-1w3fpd7-0 pgLAT")

Authors


# In[636]:


Authors_Name = []

for i in Authors:
    i=i.get_text().replace('\n', "")
    i=i.strip(" ")
    Authors_Name.append(i)
Authors_Name


# In[637]:


Published = Soup.find_all('span',class_="sc-1thf9ly-2 bKddwo")

Published


# In[639]:


Published_Date  = []

for i in Published:
    i=i.get_text().replace('\n', "")
    i=i.strip(" ")
    Published_Date .append(i)
Published_Date


# In[643]:


url = []

for i in soup.find_all('a',class_="sc-5smygv-0 nrDZj"):
    url.append(i.get('href'))
url


# In[650]:


df=pd.DataFrame({'Paper_Title':Paper_title,'Authors':Authors_Name,'Published_Date':Published_Date ,'Paper_URL':url})


# In[651]:


df


# # Q9 Write a python program to scrape mentioned details from dineout.co.in :

# In[659]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

page


# In[660]:


soup = BeautifulSoup(page.content)
soup


# Scraping Restaurant name

# In[668]:


Restaurant_name=[]
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    Restaurant_name.append(i.text)
    
Restaurant_name


# # Cuisine

# In[716]:


Cuisine = []

for i in soup.find_all('div',class_="detail-info"):
    Cuisine.append(i.text.split('|')[1])
    
Cuisine
    


# # Location

# In[717]:


Location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    Location.append(i.text)
    
Location


# # Ratings

# In[718]:


Ratings=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    Ratings.append(i.text)
    
Ratings


# # Image URL

# In[719]:


Images = []

for i in soup.find_all('img',class_="no-img"):
    Images.append(i.get('data-src'))
    
Images


# In[720]:


print(len(Restaurant_name),len(Cuisine),len(Location),len(Ratings),len(Images))


# In[721]:


df = pd.DataFrame({'Restaurant name':Restaurant_name,'Cuisine':Cuisine,'Location':Location,'Ratings':Ratings,'Image URL':Images})


# In[722]:


df


# In[723]:


df.to_csv('Restaurant_details.csv')


# # Q10) Write a python program to scrape the details of top publications from Google Scholar from
# https://scholar.google.com/citations?view_op=top_venues&hl=en

# In[31]:


Page = requests.get('https://scholar.google.com/citations?view_op=top_venues&')
page


# In[8]:


soup = BeautifulSoup(page.content)

soup


# In[28]:


Rank = soup.find_all('td',class_="gsc_mvt_p")

Rank


# In[29]:


rank  = []

for i in Rank:
    i=i.get_text().replace('\n', "")
    i=i.strip(" ")
    rank.append(i)
rank


# In[30]:


h5index = soup.find_all('td',class_="gsc_mvt_n")

h5index


# In[ ]:




