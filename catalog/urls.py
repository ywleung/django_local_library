from django.urls import path, re_path, include
from django.views.generic import RedirectView

from . import views


app_name = 'catalog'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    # path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
