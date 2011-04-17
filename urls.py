from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'zesty.comments.views.home'),
    url(r'post_comment', 'zesty.comments.views.save')
    # Examples:
    # url(r'^$', 'zesty.views.home', name='home'),
    # url(r'^zesty/', include('zesty.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
