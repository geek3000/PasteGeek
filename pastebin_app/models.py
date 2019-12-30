from django.db import models
from django.utils import timezone
# Create your models here.

class Paste(models.Model):

    title = models.CharField(max_length=30)
    paste_text= models.TextField()
    p_language = models.CharField(max_length=10, default="plaintext")
    date = models.DateTimeField(default=timezone.now(), verbose_name="Creation date")
    user = models.CharField(max_length=10)
    
    
    class Meta:
        verbose_name = "paste"
        ordering = ['date']
    
    def __str__(self):

        return self.title

class Comment(models.Model):

    name = models.CharField(max_length=10)
    comment= models.TextField()
    id_paste = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now(), verbose_name="Posted date")
    
    class Meta:
        verbose_name = "comment"
        ordering = ['date']
    
    def __str__(self):

        return self.comment