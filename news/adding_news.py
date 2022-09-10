from .iharare import iharare_dates, iharare_images_url, iharare_titles, iharare_websites_url
from .zimnews24 import zimnews24_websites_url, zimnews24_titles, zimnews24_dates, zimnews24_images_url
from .pindula import pindula_dates, pindula_titles, pindula_images_url, pindula_websites_url
from .models import News

dates = iharare_dates + zimnews24_dates + pindula_dates
images = iharare_images_url + zimnews24_images_url + pindula_images_url
titles = iharare_titles + zimnews24_titles + pindula_titles
websites_url = iharare_websites_url + zimnews24_websites_url + pindula_websites_url
new_dates = []


def add_news():
    for title, website_url, image, date in zip(titles, websites_url, images, dates):
        new = News(title=title, link=website_url, image=image, date_posted=date)
        new.save()