from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.conf import settings
import blog_post.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', lambda x: HttpResponseRedirect('/blog/douchness')),
    url(r'blog/(?P<category>\w+)/$', blog_post.views.blogs),
    url(r'^register/', blog_post.views.register_user_post),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^login/$', blog_post.views.login_user),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
