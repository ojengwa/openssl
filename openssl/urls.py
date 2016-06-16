"""mapoint URL Configuration.

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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

from tastypie.api import Api

from apps.api import resource

api = Api(api_name=settings.TASTYPIE_API_VERSION)

api.register(resource.UserResource())
api.register(resource.DomainResource())
api.register(resource.CertificateResource())


urlpatterns = (
    url(r'^api/', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', TemplateView.as_view(template_name='map.html')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
