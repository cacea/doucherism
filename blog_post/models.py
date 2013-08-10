from django.db import models
from django.conf import settings

# Create your models here.

"""
Simple model to handle blog posts
"""
class Category(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50)

class BlogEntry(models.Model):
    
    def __unicode__(self):
        return self.blog_post_name

    blog_post_name = models.CharField(max_length=200)
    blog_post_content = models.CharField(max_length=1024)
    blog_pub_date = models.DateTimeField(auto_now=True)
    blog_post_image = models.ImageField(upload_to = settings.MEDIA_ROOT, default = '/media_files/douche.jpg')
    blog_post_category = models.ForeignKey(Category)
