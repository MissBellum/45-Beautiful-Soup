from bs4 import BeautifulSoup
import requests

# with open("website.html", "r") as data:
#     contents = data.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.name)
#
# all_tags = soup.find_all(name="a")
# print(all_tags)
#
# # getText used in loops to get items inside html tags
# for tag in all_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# # used to find one item
# head = soup.find(name="h1", id="name")
# print(head)
# section = soup.find(name="h3", class_="heading")
# print(section.get("class"))
# # to get the first matching item
# url = soup.select_one(selector="p strong")
# print(url.getText())
# url_id = soup.select_one(selector="#name")
# print(url_id.text)
# # using css '.' selector
# url_h = soup.select_one(selector=".heading")
# print(url_h)

response = requests.get("https://news.ycombinator.com/")
webpage_data = response.text
# print(webpage_data)
soup = BeautifulSoup(webpage_data, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
texts = []
links = []

for tag in articles:
    text = tag.getText().split("(")[0]
    link = tag.find(name="a").get("href")
    texts.append(text)
    links.append(link)

upvote = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]
top_vote = max(upvote)
top_index = upvote.index(top_vote)
print(texts[top_index], links[top_index])
# print(texts)
# print(links)
# print(upvote)
