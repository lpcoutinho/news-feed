import pandas as pd
import utils
from scrapper import Scrapper
from datetime import datetime


############## Starting to scrape ##############
print("Starting to scrape..")
netflix_articles = Scrapper.get_netflix_articles()

# articles about software_engineering
software_engineering_articles = netflix_articles

# number of articles
print(f"Scraped {len(software_engineering_articles)} software engineering articles.")

# list to save rows dataframe
linhas_df = []

# get titles & links
for scraped_article in software_engineering_articles:
    title = {scraped_article.title}
    link = {scraped_article.link}

    # dicty for each row of dataframe
    current_date = datetime.now().strftime("%Y-%m-%d")
    linha_dict = {"Title": title, "Category": "Software Engineering", "Link": link, "Date":current_date}

    # append row to dataframe
    linhas_df.append(linha_dict)

# create dataframe
df = pd.DataFrame(linhas_df)
print(df)

# the file name
file_name = utils.file_name()

# save dataframe as CSV
df.to_csv(file_name, index=False)
