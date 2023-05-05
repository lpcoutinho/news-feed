import random
import requests
# import xmltodict
import pprint

from bs4 import BeautifulSoup
from collections import namedtuple
from urllib.request import urlopen

Article = namedtuple("Article", "title link")

NETFLIX_ENGINEERING = "https://netflixtechblog.com"

def get_netflix_articles():
    articles = []
    page = requests.get(NETFLIX_ENGINEERING)
    soup = BeautifulSoup(page.content, "html.parser")
    articles_container = soup.find_all("div", class_="u-marginBottom40 js-collectionStream")[0]
    articles_sections = []
    for article_section in articles_container.find_all("div", class_="streamItem streamItem--section js-streamItem"):
        articles_sections.append(article_section)
    for section in articles_sections:
        for element in section.find_all("a"):
            if element.has_attr("data-post-id"):
                articles.append(
                    Article(
                        title=element.find_all("div")[0].text,
                        link=element["href"]
                    )
                )
    return articles[0:3]

################## Starting to scrape #########################
print("Starting to scrape..")
netflix_articles = get_netflix_articles()

software_engineering_articles =  netflix_articles 

print(f"Scraped {len(software_engineering_articles)} software engineering articles.")
print("Sending Email")

email_body = "Here are all your recent articles: \n"
email_body += "\n \n \n SOFTWARE ENGINEERING \n \n \n"
for scraped_article in software_engineering_articles:
    email_body += f"{scraped_article.title} {scraped_article.link} \n"

print("Done sending email")
print(email_body)
