from django.urls import path

from .views import *


urlpatterns = [
    path('list/', list_view, name='list'),
    path('', home_view, name='home'),
]
