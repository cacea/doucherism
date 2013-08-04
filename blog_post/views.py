from django.shortcuts import render
from blog_post.models import BlogEntry
from blog_post.forms import BlogPostForm
from django.shortcuts import HttpResponseRedirect
from time import gmtime, strftime

# Create your views here.
"""
This method will display all user posts (newest first)
"""
def home(request):
    blog_template = "blogs.html"
    list_all_posts = BlogEntry.objects.all().order_by('-blog_pub_date').values() # List all posts on DB ordered by date (newest first).
    return render(request, blog_template, locals())

"""
We will provide the user with a form to upload a post. 
3 fields are available: post name, post data and the file upload option.
the blog_pub_date is automatically set by DB.
"""
def register_user_post(request):
    register_user_template = "register_post.html"
    if request.method == "POST":
            new_blog_post = BlogPostForm(request.POST, request.FILES)
            if new_blog_post.is_valid():
                new_blog_post.save()
                return HttpResponseRedirect('/')
    else:
        form = BlogPostForm()
    return render(request, register_user_template, locals())
