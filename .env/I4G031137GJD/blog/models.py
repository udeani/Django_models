from optparse import TitledHelpFormatter
from tabnanny import verbose
from typing import Text
from django.db import models
from django.conf import settings
#from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    # class Meta:
    #     verbose_name = "Post"
    #     verbose_name_plural = "Post"
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()