# this file manages the routing the urls in this app ( scwebapp )

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='scwebapp-home'),
    path('recipes/', views.recipes, name='scwebapp-recipes'),
    # path('about/', views.about, name='scwebapp-about'),
]
