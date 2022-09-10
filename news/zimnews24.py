from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


zimnews24_images_url = []
zimnews24_websites_url = []
zimnews24_titles = []
zimnews24_dates = []


my_url = "https://zimnews24.com/index.php/category/local-news/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "archive-grid-post"})
for container in containers:
    image = container.div.div.img["src"]
    zimnews24_images_url.append(image)
    details = container.div.findAll("div", {"class": "pad read-details color-tp-pad"})
    for detail in details:
        dates = detail.findAll("div", {"class": "post-item-metadata entry-meta"})
        for date in dates:
            elements = date.span.findAll("span", {"class": "item-metadata posts-date"})
            for actual_date in elements:
                zimnews24_dates.append(actual_date.text.strip())
        titles = detail.findAll("div", {"class": "read-title"})
        for title in titles:
            zimnews24_titles.append(title.h4.a["href"])
            zimnews24_websites_url.append(title.h4.a.text)