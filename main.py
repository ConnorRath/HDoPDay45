from bs4 import BeautifulSoup
import pprint
import numpy
import lxml
import requests

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# heading = soup.find(name='h1', id='name')
# section_heading = soup.find(name='h3', class_="heading")
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# print(heading)
#
# company_url = soup.select_one(selector='p a')
# print(company_url)
#
# form_tag = soup.find("input")
#
# pick_by_id = soup.select_one(selector='#name')
#
# pick_by_class = soup.select('.heading')


#-------------^^^^^^^^^^^WARM_UP^^^^^^^^^^^^^----------------#

url = "https://news.ycombinator.com/"

response = requests.get(url)

data = response.text
soup = BeautifulSoup(data, "html.parser")
# print(soup.find_all)

score_list = soup.find_all(class_="score")
#print(score_list)

article_tag = soup.find(name='span', class_='titleline')
# print(article_tag.a)
#article_text = soup.select_one(".titleline a")
# article_upvote = soup.select_one(".subline .score")


article_texts = []
article_links = []

all_article_tags = soup.find_all(name='span', class_='titleline')
all_article_scores = soup.find_all(name='span', class_='score')

for article_tag in all_article_tags:
    text = article_tag.a.getText()
    article_texts.append(text)
    link = article_tag.a.get('href')
    article_links.append(link)

# The below for loop is correct, however the single line below it is called "Loop comprehension" and is cleaner, does
# and the same thing
# for upvote in all_article_upvotes:
#     article_upvotes.append(upvote.getText())

article_scores_num = [int(score.getText().split(' ')[0]) for score in all_article_scores]

print(article_texts)
print(article_links)
# article_scores_num = sorted(article_scores_num, reverse=True)
print(article_scores_num)

######## Personal project, find a way to sort the list of upvotes, find the indices of that list, and sort the
######## articles in that same order. DONE!!

largest_number = max(article_scores_num)
largest_index = article_scores_num.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_index)

sorted_index = numpy.argsort(numpy.array(article_scores_num))[::-1]
print(sorted_index)

for index in sorted_index:
    print(f"{article_texts[index]}, {article_links[index]}, {article_scores_num[index]}\n")
