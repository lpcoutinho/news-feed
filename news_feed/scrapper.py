from collections import namedtuple

import requests
from bs4 import BeautifulSoup

Article = namedtuple("Article", "title link")
NETFLIX_ENGINEERING = "https://netflixtechblog.com"


class Scrapper:
    def __init__(self):
        pass

    # get netflix articles
    def get_netflix_articles():
        articles = []
        page = requests.get(NETFLIX_ENGINEERING)
        soup = BeautifulSoup(page.content, "html.parser")
        articles_container = soup.find_all(
            "div", class_="u-marginBottom40 js-collectionStream"
        )[0]
        articles_sections = []
        for article_section in articles_container.find_all(
            "div", class_="streamItem streamItem--section js-streamItem"
        ):
            articles_sections.append(article_section)
        for section in articles_sections:
            for element in section.find_all("a"):
                if element.has_attr("data-post-id"):
                    articles.append(
                        Article(
                            title=element.find_all("div")[0].text, link=element["href"]
                        )
                    )
        return articles[0:3]
