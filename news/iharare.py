from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from datetime import datetime
import calendar
from datetime import date


today = datetime.now()
current_month_name = calendar.month_name[date.today().month]
current_month_abb = today.strftime("%b")


iharare_images_url = []
iharare_websites_url = []
iharare_titles = []
iharare_dates = []

my_url = "https://iharare.com/"
uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "item-inner clearfix"})
for container in containers:
    image = container.div.find('a', style=True)
    iharare_images_url.append(image["style"][22:-2])
    iharare_titles.append(container.h2.text.strip())
    iharare_websites_url.append(container.h2.a["href"])
    # summaries = container.findAll("div", {"class": "post-summary"})
    # for summary in summaries:
    #     print(summary.text.strip())
    meta_data = container.findAll("div", {"class": "post-meta"})
    for meta in meta_data:
        date = meta.span.time.text
        new_date = date.replace(current_month_abb, current_month_name)
        iharare_dates.append(new_date)
