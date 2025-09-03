from bs4 import BeautifulSoup
import requests

responce = requests.get("https://news.ycombinator.com/news")
responce.raise_for_status()
yc_web_page = responce.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="tr", class_="athing")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.find("span", class_="titleline").getText()
    article_texts.append(text)
    link = article_tag.find("span", class_="titleline").find("a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# Challange print the link and title of the highes score "article_upvotes"

# My solution
high_score = 0
article_index = 0
for index, score in enumerate(article_upvotes):
    if score > high_score:
        high_score = score
        article_index = index

print(article_texts[article_index])        
print(article_links[article_index])
print(article_upvotes[article_index],"\n")

# Lesson solution using the max() method
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])