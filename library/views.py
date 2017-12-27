from django.views.generic import (ListView, CreateView, DeleteView, DetailView, UpdateView)
from django.urls import reverse_lazy
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from .forms import BookForm, CategoryForm, AuthorForm
from .models import Book, Category, Author
from django.db.models import Q
from user.decorators import class_login_required, require_authenticated_permission

class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'
    
    
    def get_queryset(self):
        queryset = Author.objects.all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query)|
                Q(last_name__icontains=query)
            ).distinct()
        return queryset
    

class AuthorDetail(DetailView):
    model = Author
    template_name = 'author_detail.html'
    
    
class AuthorUpdate(UpdateView):
    model = Author
    template_name = 'author_form_update.html'
    form_class = AuthorForm
    
@require_authenticated_permission('library.add_author')
class AuthorCreate(CreateView):
    form_class = AuthorForm
    model = Author
    template_name = 'author_form.html'
   

class BookList(ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        queryset = Book.objects.all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)|
                Q(authors__first_name__icontains=query)|
                Q(authors__last_name__icontains=query)|
                Q(category__name__icontains=query)
            ).distinct()
        return queryset
    
   
@require_authenticated_permission('library.add_book')
class BookCreate(CreateView):
    form_class = BookForm
    model = Book
    template_name = 'book_form.html'
    
class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'

@require_authenticated_permission('library.delete_book')
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('library_book_list')
    template_name = 'book_confirm_delete.html'

@require_authenticated_permission('library.change_book')
class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form_update.html'
    
class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    
    def get_queryset(self):
        queryset = Category.objects.all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)
            ).distinct()
        return queryset
    
@require_authenticated_permission('library.add_category')
class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name='category_form.html'
    
class CategoryDetail(DetailView):
    model = Category
    template_name = 'category_detail.html'
    
@require_authenticated_permission('library.delete_category')
class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('library_category_list')
    template_name = 'category_confirm_delete.html'

@require_authenticated_permission('library.change_category')
class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form_update.html'

def json(request):
    query = Book.objects.all()  
    query = serializers.serialize('json', query)
    return HttpResponse(query, content_type="application/json")
