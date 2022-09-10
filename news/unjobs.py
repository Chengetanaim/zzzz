from bs4 import BeautifulSoup as soup
from urllib.request import Request
from urllib.request import urlopen as uReq

my_url = "https://unjobs.org/duty_stations/zimbabwe"

un_links = []
un_titles = []
req = Request(
    url='https://unjobs.org/duty_stations/zimbabwe',
    headers={'User-Agent': 'Mozilla/5.0'}
)

uClient = uReq(req)
page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("a", {"class": "jtitle"})
for container in containers:
    un_links.append(container["href"])
    un_titles.append((container.text))