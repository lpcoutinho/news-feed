# News Feed

App to scrape a few interesting websites for articles on a daily basis. 

### Tools
- Python
- BeautifulSoup 
- Cron
- MailGun 

### To Do
- [x] Add Articles in CSV
- [ ] Add Cron to schedule
- [ ] Send somehow. E-mail, telegram, etc
- [ ] Add https://eng.uber.com
- [ ] Add https://engineeringblog.yelp.com/
- [ ] Add https://engineering.fb.com/feed/
- [ ] Add https://www.databricks.com/blog/category/engineering

**This App was Created for Learning Purposes**

Please feel free to use whatever you need to help you get a better understanding of Python/BeautifuSoup/WebScrapping

## Install & Run this project

- Clone this repository

I like to work with Poetry, Makefile and another tools if you also use it to install the requirements of this project, just use `make install`.

In other cases you will need to create a virtual environment and install the requirements with pip.

- Create Virtual Env
```bash
python -m venv venv
```
- Install requirements

```bash
pip install -r requirements.txt
```
- Run app
```bash
python news_feed/app.py
```