"""djviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from .views import home, download, response, laredirect
#from blog.views import post_model_list_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('download/', download, name='download'),
    path('response/', response, name='response1'),
    path('redirect/', laredirect, name='redirect'),

    path('blog/', include('blog.urls')) # app controls all urls
    #path('post/', post_model_list_view),
]
