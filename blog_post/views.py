from django.shortcuts import render
from blog_post.models import BlogEntry
from blog_post.forms import BlogPostForm
# Create your views here.

def home(request):
    blog_template = "blogs.html"
    list_all_posts = BlogEntry.objects.all() # Con esto se listan todos los elementos de que se encuentren en la DB
    return render(request, blog_template, locals())

def register_user_post(request):
    register_user_template = "register_post.html"
    if request.method == "POST":
        if form.is_valid():
            form.save(request.POST)
    else:
        form = BlogPostForm()
    return render(request, register_user_template, locals())
