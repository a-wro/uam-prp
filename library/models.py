from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField
# Create your models here.

class Category(models.Model):
    class Meta:
        ordering = ['name']
    
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31, unique=True)
    
    def printBooks(self):
        query = self.book_set.all()
        books = ''
        for book in query:
            books += "{}\n".format(book.title)
        return books
            
    
    def get_absolute_url(self):
        return reverse('library_category_detail', kwargs={'slug': self.slug})
        
    def get_delete_url(self):
        return reverse('library_delete_category', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('library_update_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=31)
    category = models.ManyToManyField(Category, blank=True)
    slug = models.SlugField(max_length=31, unique=True)
    price = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11,)
    description = models.TextField(default='')
    
    def get_absolute_url(self):
        return reverse('library_book_detail', kwargs={'slug': self.slug})
        
    def get_delete_url(self):
        return reverse('library_delete_book', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('library_update_book', kwargs={'slug': self.slug})
    
    def printCategories(self):
        categories = ''
        query = self.category.all()
        for c in query:
            categories += c.name.title()
            if c != query.last():
                categories += ", "
        
        return categories
    
    def __str__(self):
        return self.title
        

    
    

    
 
