from .iharare_jobs import iharare_jobs_links, iharare_jobs_titles
# from .jobszimbabwe import jobszimbabwe_dates, jobszimbabwe_links, jobszimbabwe_titles
# from .unjobs import un_links, un_titles
from .models import Job



titles = iharare_jobs_titles 
links = iharare_jobs_links 


def add_job():
    for title, link in zip(titles, links):
        new = Job(title=title, link=link)
        new.save()
