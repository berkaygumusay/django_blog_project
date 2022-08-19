from enum import auto
from turtle import mode
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    articleImage = models.FileField(blank=True,null=True,verbose_name="Upload Image To Article")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-createdDate']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Article",related_name="comments")
    commentAuthor = models.CharField(max_length=50,verbose_name="Username")
    commentContent = models.CharField(max_length=200,verbose_name="Comment")
    commentDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.commentContent
    class Meta:
        ordering = ['-commentDate']