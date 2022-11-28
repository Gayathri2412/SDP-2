from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),

    path('book', views.book, name='book'),
    path('contact', views.contact, name='contact'),
    path('signup',views.signup,name='signup'),
    path('signin', views.signin, name='signin'),

]

urlpatterns += staticfiles_urlpatterns()
