from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updatet_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    is_published = models.BooleanField(default=True)
