"""p1 URL Configuration

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
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from books import views
from signup.views import signaction
from login.views import loginaction
from contact.views import contact
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('book', views.book, name='book'),
    path('book2', views.book2, name='book2'),
    path('contact', contact, name='contact'),
    path('con', views.con, name='con'),
    path('signup/', signaction, name='up'),
    path('login/', loginaction, name='in'),
    path('logout/', views.logout, name='out'),
    path('des/', views.des, name='des'),
    path('des1/', views.des1, name='des1'),
    path('des2/', views.des2, name='des2'),
    path('des3/', views.des3, name='des3'),
    path('des4/', views.des4, name='des4'),
    path('des/b/', views.b, name='b'),
    path('des1/b/', views.b, name='b'),
    path('des2/b/', views.b, name='b'),
    path('des3/b/', views.b, name='b'),
    path('des4/b/', views.b, name='b'),
    path('des/b/pay/', views.pay, name='pay'),
    path('des1/b/pay/', views.pay, name='pay'),
    path('des2/b/pay/', views.pay, name='pay'),
    path('des3/b/pay/', views.pay, name='pay'),
    path('des4/b/pay/', views.pay, name='pay'),
]
urlpatterns += staticfiles_urlpatterns()
