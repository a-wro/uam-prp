"""prp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
import library.urls as library_urls
from user import urls as user_urls
from .views import redirect_root
from library.views import json

from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm


urlpatterns = [
  url(r'^$', redirect_root),
  url(r'^library/', include(library_urls)),
  url(r'^admin/', admin.site.urls),
  url(r'^index/$', json),
  url(r'^user/', include(user_urls, namespace='dj-auth')),
  


]

    
