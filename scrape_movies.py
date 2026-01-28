from bs4 import BeautifulSoup
import requests
import time
import json
import os 
from dotenv import load_dotenv

load_dotenv()
api= os.getenv("API_KEY")

# Function to scrape id of 25 popular movies for a year

def popular_movies(url):
   movies=[]
   headers = {
        "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
        )
    }
   response = requests.get(url,headers=headers)
   soup = BeautifulSoup(response.content, "html.parser")
   review_blocks = soup.find_all("a", class_="ipc-title-link-wrapper")
   for r in review_blocks :
    title = r.get("href")
    movies.append(title.split("/")[2]) # 
   return movies

# fetching popular movies
years =list(range(2020,2026,1))
yearlist ={}
for year in years:
  m_list =popular_movies(f"https://www.imdb.com/search/title/?explore=genres&title_type=feature&release_date={year}-01-01,{year}-12-31&user_rating=6,10&num_votes=25000,")
  yearlist[year]=m_list
  print(f"✅ Fetched for {year}")
  time.sleep(2)
# print(yearlist)


movie_list ={}
for year in yearlist:
  movies=[]
  for id in yearlist[year]:
    print(id)
    omdb_url = f"http://www.omdbapi.com/?apikey={api}&i={id}"
    response = requests.get(omdb_url)
    data = response.json()
    print(data)
    movies.append({"id":id,"title":data["Title"],"rating":data["imdbRating"],"genre":data["Genre"],"actors":data["Actors"],"directors":["Director"]})
  movie_list[year]=movies

# dump dict into json
with open("movie_list.json", "w", encoding="utf-8") as f:
    json.dump(movie_list, f, ensure_ascii=False, indent=4)