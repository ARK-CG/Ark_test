from django.urls import path, include
from . import views

app_name = 'ark_web'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('news', views.news, name='news'),
    path('idea', views.idea, name='idea'),
    path('progress', views.progress, name='progress'),
]
