from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

def popular_movies(url):
   movies=[]
   headers = {
        "User-Agent": "Mozilla/5.0"
    }
   response = requests.get(url,headers=headers)
   soup = BeautifulSoup(response.content, "html.parser")
   review_blocks = soup.find_all("h3", class_="ipc-title__text ipc-title__text--reduced")
   for r in review_blocks :
    title = r.text
    movies.append(title)
   return movies

# fetching popular movies
years =[2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
yearlist ={}
for year in years:
  m_list =popular_movies(f"https://www.imdb.com/search/title/?explore=genres&title_type=feature&release_date={year}-01-01,{year}-12-31&user_rating=6,10&num_votes=25000,")
  yearlist[year]=m_list
  time.sleep(2)
print(yearlist)
for m in yearlist:
  yearlist[m].remove("Recently viewed")

id_list ={}
for m in yearlist:
  movies=[]
  for i in yearlist[m]:
    i = " ".join(i.split()[1:])
    omdb_url = f"http://www.omdbapi.com/?apikey=2fd35f7f&t={i}"
    response = requests.get(omdb_url)
    data = response.json()
    movies.append({"id":data["imdbID"],"title":i,"rating":data["imdbRating"],"genre":data["Genre"]})
  id_list[m]=movies

# dump dict into json