from django.shortcuts import render
from .models import News, Job
from .serializers import NewsSerializer, JobSerializer
from datetime import datetime
from rest_framework import generics
from django.http import HttpResponse
from .jobs import add_job
from .adding_news import add_news

today = datetime.now()


class NewsList(generics.ListAPIView):
    queryset = News.objects.filter(date_posted__contains=today.strftime("%b")).order_by('-date_posted')
    serializer_class = NewsSerializer

    # search_fields = ('^')


class JobList(generics.ListAPIView):
    queryset = Job.objects.order_by('-id')
    serializer_class = JobSerializer


def update(request):
    add_job()
    add_news()

    return HttpResponse("Updated!")