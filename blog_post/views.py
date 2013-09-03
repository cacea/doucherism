from django.shortcuts import render
from blog_post.models import BlogEntry, Category
from blog_post.forms import BlogPostForm
from django.shortcuts import HttpResponseRedirect, redirect
from time import gmtime, strftime
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

# Create your views here.
"""
This method will display all user posts (newest first)
"""
def blogs(request, category):
    blog_template = "blogs.html"
    list_all_posts = BlogEntry.objects.filter(blog_post_category__name = category).order_by('-blog_pub_date').values('blog_post_name', 'blog_post_content', 'blog_post_category__name', 'blog_post_image') # List all posts on DB ordered by date (newest first).
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

def login_user(request):
    template = "login.html"
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                pass
    else:
        return render(request, template, locals())

