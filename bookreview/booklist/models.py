from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 200)
    wordcount = models.IntegerField()
    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    author = models.CharField(max_length = 200)
    content = models.CharField(max_length = 5000)
    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.book.title + ' | ' + self.author + ' | ' + self.content[:20]