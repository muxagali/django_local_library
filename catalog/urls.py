from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # "catalog/" page
    url(r'^$', views.index, name='index'),
    # Bokks list page
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    # Book detail  
    # update, create and delete Authors
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^book/create$', views.BookCreate.as_view(), name='book-create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book-update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book-delete'),
    
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    # Authors details
     # update, create and delete Authors
     url(r'^author/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
    
    # Authentication page
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^borrowed/$', views.AllBorrowedByUserListView.as_view(), name='all-borrowed'),
    
    # Validation HTML forms
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
   
]