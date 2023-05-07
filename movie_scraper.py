from bs4 import BeautifulSoup
import numpy
import pprint
import requests
import json

url = "https://www.empireonline.com/movies/features/best-movies-2/"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
script = soup.find("script", type='application/json')
data = json.loads(script.string)
#print(soup.prettify())
movie_title = soup.select_one(selector="body div main article.jsx-1456218620 .article-content.jsx-1456218620 "
                                       ".listicle-container.jsx-3523802742 .listicle-item.jsx-3523802742")
titles = soup("body div main article.jsx-1456218620 .article-content.jsx-1456218620 "
                                       ".listicle-container.jsx-3523802742 .listicle-item.jsx-3523802742")
# print(movie_title)
movie_list = []

for film in data["props"]["pageProps"]["data"]["getArticleByFurl"]["_layout"][3]['content']['images']:
    movie_list.append(film['titleText'])

movie_list.reverse()
print(movie_list)

