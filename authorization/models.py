from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    published_date = models.DateField()

    def __str__(self) -> str:
        return self.title
