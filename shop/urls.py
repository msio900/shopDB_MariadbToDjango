"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('custlist', views.custlist, name='custlist'),
    path('custdetail', views.custdetail, name='custdetail'),
    path('custdelete', views.custdelete, name='custdelete'),
    path('custadd', views.custadd, name='custadd'),
    path('custaddimpl', views.custaddimpl, name='custaddimpl'),
    path('custupdateimpl', views.custupdateimpl, name='custupdateimpl'),
    path('custupdate', views.custupdate, name='custupdate'),
    path('itemlist', views.itemlist, name='itemlist'),
    path('itemadd', views.itemadd, name='itemadd'),
    path('itemaddimpl', views.itemaddimpl, name='itemaddimpl'),
    path('itemdetail', views.itemdetail, name='itemdetail'),
    path('itemdelete', views.itemdelete, name='itemdelete'),
    path('itemupdate', views.itemupdate, name='itemupdate'),
    path('itemupdateimpl', views.itemupdateimpl, name='itemupdateimpl'),
]
