from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(upload_to='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail_url', kwargs={'pk': self.pk})