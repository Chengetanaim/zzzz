from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq



jobszimbabwe_links = []
jobszimbabwe_titles = []
jobszimbabwe_dates = []

my_url = "https://jobszimbabwe.co.zw/"


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "loop-item-wrap list"})
for container in containers:
    jobszimbabwe_links.append(container.div.h3.a["href"])
    jobszimbabwe_titles.append(container.div.h3.a.text)
    dates = container.findAll("div", {"class": "show-view-more"})
    for date in dates:
        jobszimbabwe_dates.append(date.span.text)
