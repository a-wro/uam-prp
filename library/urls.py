from django.conf.urls import url
from .views import (BookCreate, BookList, BookDetail, BookDelete, BookUpdate,
   CategoryDetail, CategoryList, CategoryDelete, CategoryUpdate, CategoryCreate)

urlpatterns = [
  url(r'^$', BookList.as_view(), name='library_book_list'),
  url(r'^create/$', BookCreate.as_view(), name='library_create_book'),
  url(r'^book/(?P<slug>[\w\-]+)/$', BookDetail.as_view(), name='library_book_detail'),
  url(r'^book/(?P<slug>[\w\-]+)/delete/$', BookDelete.as_view(), name='library_delete_book'),
  url(r'^book/(?P<slug>[\w\-]+)/update/$', BookUpdate.as_view(), name='library_update_book'),
  url(r'^category/$', CategoryList.as_view(), name='library_category_list'),
  url(r'^category/create/$', CategoryCreate.as_view(), name='library_create_category'),
  url(r'^category/(?P<slug>[\w\-]+)/$', CategoryDetail.as_view(), name='library_category_detail'),
  url(r'^category/(?P<slug>[\w\-]+)/delete/$', CategoryDelete.as_view(), name='library_delete_category'),
  url(r'^category/(?P<slug>[\w\-]+)/update/$', CategoryUpdate.as_view(), name='library_update_category'),
]
