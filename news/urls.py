from django.urls import path
from .views import NewsList, JobList
from . import views


urlpatterns = [
    path('news/', NewsList.as_view()),
    path('jobs/', JobList.as_view()),
    path('update/', views.update),
]