from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    image = models.URLField()
    date_posted = models.CharField(max_length=20)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    date_posted = models.CharField(max_length=100, default="null")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title