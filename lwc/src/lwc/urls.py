"""lwc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'doge.views.home', name='home'),
    url(r'^contact/$', 'doge.views.contact', name='contact'),
    url(r'^about/$', 'lwc.views.about', name='about'),
    url(r'^cat/$', 'lwc.views.cat', name='cat'),
    url(r'^parallax/$', 'lwc.views.parallax', name='parallax'),
  #  url(r'^home2/$', 'lwc.views.home2', name='home2'),   
    #from django redux right below this line
    url(r'^accounts/', include('registration.backends.default.urls')),

] 

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
