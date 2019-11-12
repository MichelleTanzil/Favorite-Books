from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books),
    url(r'^add_book/(?P<user_id>\d+)$', views.add_book),
    url(r'^books/(?P<book_id>\d+)$', views.book_profile),
    url(r'^edit_book/(?P<book_id>\d+)$', views.edit_book),
    url(r'^delete_book/(?P<book_id>\d+)$', views.delete_book),
    url(r'^unfavorite/(?P<book_id>\d+)/(?P<user_id>\d+)$', views.unfavorite),
    url(r'^add_to_favorites/(?P<book_id>\d+)/(?P<user_id>\d+)$', views.add_to_favorites),
    url(r'^favorite_books$', views.favorite_books),

]
