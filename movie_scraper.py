from bs4 import BeautifulSoup
import requests
import json

url = "https://www.empireonline.com/movies/features/best-movies-2/"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
script = soup.find("script", type='application/json')
data = json.loads(script.string)
movie_list = []

for film in data["props"]["pageProps"]["data"]["getArticleByFurl"]["_layout"][3]['content']['images']:
    movie_list.append(film['titleText'])

movie_list.reverse()
print(movie_list)

