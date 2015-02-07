from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login, logout
from django.contrib.auth.models import User
# import settings
# import allot.urls
from scrapy.urls import * 
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'scrapy.views.home', name='home'),
    url(r'collage', 'scrapy.views.collage', name='collage'),
    url(r'greetings', 'scrapy.views.greetings', name='greetings'),
    url(r'calendar', 'scrapy.views.calendar', name='calendar'),
    url(r'scrapbook', 'scrapy.views.scrapbook', name='scrapbook'),
    url(r'faq', 'scrapy.views.faq', name='faq'),
    url(r'about', 'scrapy.views.about', name='about'),
    url(r'form', 'scrapy.views.form', name='form'),
    url(r'thankyou', 'scrapy.views.thankyou', name='thankyou'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)