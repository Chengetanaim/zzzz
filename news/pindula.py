from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

pindula_images_url = []
pindula_websites_url = []
pindula_titles = []
pindula_dates = []

my_url = "https://news.pindula.co.zw/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("article")
for container in containers:
    pindula_websites_url.append(container.a["href"])
    pindula_images_url.append(container.a.img["src"])
    pindula_titles.append(container.h2.a.text)
    meta_data = container.find("div", {"class": "entry-meta"})
    for data in meta_data:
        if '2022' in data.text.strip():
            pindula_dates.append(data.text.strip())

