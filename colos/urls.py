from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('2048_data/', views.getData, name='2048_data'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('pricing', views.pricing, name='pricing'),
    path('schedule', views.schedule, name='schedule'),
    path('single_post', views.single_post, name='single_post'),
    path('speakers', views.speakers, name='speakers'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('2048', views.game, name='game'),
]