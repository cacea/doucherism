from django.contrib import admin
from blog_post.models import BlogEntry, Category 

admin.site.register(BlogEntry)
admin.site.register(Category)
