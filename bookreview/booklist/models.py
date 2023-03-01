from django.db import models

# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length = 200)
    publish_date = models.DateTimeField('date published')