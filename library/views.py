from django.views.generic import (ListView, CreateView, DeleteView, DetailView, UpdateView)
from django.urls import reverse_lazy
from django.core import serializers
from django.http import HttpResponse

from .forms import BookForm, CategoryForm
from .models import Book, Category


class BookList(ListView):
    model = Book
    template_name = 'book_list.html'

class BookCreate(CreateView):
    form_class = BookForm
    model = Book
    template_name = 'book_form.html'
    
class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('library_book_list')
    template_name = 'book_confirm_delete.html'

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form_update.html'

class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    
class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name='category_form.html'
    
class CategoryDetail(DetailView):
    model = Category
    template_name = 'category_detail.html'
    
class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('library_category_list')
    template_name = 'category_confirm_delete.html'

class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form_update.html'
    
def json(request):
    query = Book.objects.all()  
    query = serializers.serialize('json', query)
    return HttpResponse(query, content_type="application/json")
