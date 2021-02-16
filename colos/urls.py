from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('pricing', views.pricing, name='pricing'),
    path('schedule', views.schedule, name='schedule'),
    path('single_post', views.about, name='single_post'),
    path('speakers', views.speakers, name='speakers'),
    path('sponsors', views.about, name='sponsors'),
]