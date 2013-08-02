from django.forms import ModelForm
from blog_post.models import BlogEntry

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['blog_post_name', 'blog_post_content', 'blog_post_image']