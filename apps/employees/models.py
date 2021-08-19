from django.db import models
from django.urls import reverse

class Employee(models.Model):

    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    information = models.TextField()

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('employee_detail_url', kwargs={'pk': self.pk})
