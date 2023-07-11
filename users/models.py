from django.db import models

class NewsArticle(models.Model):
    """This class creates the model (table) in database """
    title = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    source = models.CharField(max_length=255)

