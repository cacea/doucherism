from django.db import models

# Create your models here.

class BlogEntry(models.Model):
    
    def __unicode__(self):
        return self.blog_post_name

    blog_post_name = models.CharField(max_length=200)
    blog_post_content = models.CharField(max_length=1024)
    blog_pub_date = models.DateTimeField('date published')
