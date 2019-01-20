from django.conf import settings
from django.db import models
from django.utils import timezone


class course(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length = 500)
    domain = models.CharField(max_length = 200) 
    link = models.CharField(max_length=200)
    price = models.IntegerField(default = 0)
    duration = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)
    star = models.IntegerField(default = 0)
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    #def publish(self):
     #   self.published_date = timezone.now()
     #   self.save()

    def __str__(self):
        return self.name
