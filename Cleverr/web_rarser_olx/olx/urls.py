from django.urls import path

from .views import IndexView, ParserView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('parsing/', ParserView.as_view(), name='parser')
]