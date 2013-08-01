from django.conf.urls import patterns, include, url
import blog_post.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', blog_post.views.home),
    url(r'^register/', blog_post.views.register_user_post),
    url(r'^admin/', include(admin.site.urls)),
)
