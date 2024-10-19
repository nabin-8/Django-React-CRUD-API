from django.urls import path
from .views import get_Books


urlpatterns = [
    path('books/', get_books, name='get_books')
]
