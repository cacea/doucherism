from django.conf.urls import patterns, include, url
from django.conf import settings
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

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
            #(r'^media_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT#, 'show_indexes':True#}),
)
