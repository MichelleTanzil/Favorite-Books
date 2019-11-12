from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    # List of books page
    url(r'^books$', views.books),
    # Add a new book
    url(r'^add_book/(?P<user_id>\d+)$', views.add_book),
    # Profile of 1 book
    url(r'^books/(?P<book_id>\d+)$', views.book_profile),
    # Edit a book
    url(r'^edit_book/(?P<book_id>\d+)$', views.edit_book),
    # Delete a book
    url(r'^delete_book/(?P<book_id>\d+)$', views.delete_book),
    # Unfavorite a book
    url(r'^unfavorite/(?P<book_id>\d+)/(?P<user_id>\d+)$', views.unfavorite),
    # Favorite a book
    url(r'^add_to_favorites/(?P<book_id>\d+)/(?P<user_id>\d+)$', views.add_to_favorites),
    # List of favorite books for the logged in user
    url(r'^favorite_books$', views.favorite_books),

]
