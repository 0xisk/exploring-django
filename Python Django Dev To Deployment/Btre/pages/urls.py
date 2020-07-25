from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing/', views.index, name='listings.urls'),
    path('about', views.about, name='about'),
]
