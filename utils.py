import json
import pandas as pd

#converting json to df
movies= None
with open("id_list.json", "r", encoding="utf-8") as f:
    movies = dict(json.load(f))

movie_dict = {"id":[],"title":[],"rating":[],"genre":[],"year":[]}

for y in movies:
    for i in movies[y]:

        movie_dict["id"].append(i["id"])
        movie_dict["title"].append(i["title"])
        movie_dict["rating"].append(i["rating"])
        movie_dict["genre"].append(i["genre"])
        movie_dict["year"].append(y)

df = pd.DataFrame(movie_dict)
df.to_csv("./data/imdb_list.csv")
# df.to_excel("./data/imdb_list.xlsx")