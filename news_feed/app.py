import requests
import pandas as pd

from bs4 import BeautifulSoup
from collections import namedtuple
from datetime import datetime

Article = namedtuple("Article", "title link")

NETFLIX_ENGINEERING = "https://netflixtechblog.com"

# get netflix articles
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

# articles about software_engineering
software_engineering_articles =  netflix_articles 

# list to save rows dataframe
linhas_df = []

# number of articles
print(f"Scraped {len(software_engineering_articles)} software engineering articles.")
print("Sending Email")

# show titles & links
email_body = "Here are all your recent articles: \n"
email_body += "\n \n \n SOFTWARE ENGINEERING \n \n \n"
for scraped_article in software_engineering_articles:
    title = {scraped_article.title}
    link = {scraped_article.link}
    email_body += f"{title} {link} \n"
   
    # dicty for each row of dataframe
    linha_dict = {"Title": title, "Category":"Software Engineering", "Link": link}
    
    # append row to dataframe
    linhas_df.append(linha_dict)
    
print("Done sending email")
print(email_body)

# create dataframe
df = pd.DataFrame(linhas_df)

# get current date
current_date = datetime.now().strftime("%Y-%m-%d")

# the file name
file_name = f"news_{current_date}.csv"

# save dataframe as CSV
df.to_csv(file_name, index=False)