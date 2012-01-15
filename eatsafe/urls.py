from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^eatsafe/', include('eatsafe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^style.css$', 'direct_to_template', {'template' : 'style.css'}),
    (r'^fakejson$',  'direct_to_template', {'template' : 'fakejson'}),
)

urlpatterns += patterns('',
    url(r'^$', 'home.views.index', name='home_index'),
)
