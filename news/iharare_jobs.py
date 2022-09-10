from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


iharare_jobs_links = []
iharare_jobs_titles = []
iharare_jobs_dates = []


my_url = "https://ihararejobs.com/?page=1"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "listings job"})
for container in containers:
    iharare_jobs_links.append("https://ihararejobs.com" + container.a["href"])
    iharare_jobs_titles.append(container.div.h3.a["title"])
    dates = container.div.find("span", {"class": "date"})
    # for date in dates:
    #     iharare_jobs_dates.append(date.text.strip())
