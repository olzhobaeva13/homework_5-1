from django.db import models
from django.urls import reverse

class Question(models.Model):

    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=13)
    your_question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name}'

    def get_absolute_url(self):
        return reverse('questions_page_url', kwargs={'pk': self.pk})
