"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static #to serve uplaoded files
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # In challenges project-> we used this method=> 
    # path('blog/',include('blog.urls')) i.e it on empty path it shows error and /blog/ gives homepage #http://localhost:8000/blog/posts/my-first-post
    #but in real time projects we need homepage on empty path. So,
    path("",include('blog.urls'))  #http://localhost:8000/
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
