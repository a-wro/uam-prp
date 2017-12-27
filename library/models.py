from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField
from django_countries.fields import CountryField
from pathlib import Path
from django.utils.text import slugify

class Author(models.Model):
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    From = CountryField(blank_label='(select country)')
    born = models.DateField(blank=True, null=True)
    url = models.URLField(default='http://awro.pythonanywhere.com/library/')
    info = models.TextField(default='')
    slug = models.SlugField(max_length=31, unique=True)
    
    def get_absolute_url(self):
        return reverse('library_author_detail', kwargs={'slug': self.slug})
        
    def get_update_url(self):
        return reverse('library_author_update', kwargs={'slug': self.slug})
        
    def fullName(self):
        return(self.first_name.title() +' ' + self.last_name.title())
        
    def __str__(self):
        return self.fullName()
        
    def genres(self):
        out = ''
        genres = []
        for b in self.book_set.all():
            for c in b.category.all():
                genres.append(c.name)
        if genres:
            genres = set(genres)
            for genre in genres:
                out += "{}, ".format(genre.title())
            
        return out
        
    def _get_unique_slug(self):
        slug = slugify(self.fullName())
        unique_slug = slug
        num = 1
        while Author.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
   
            
    def get_img_path(self):
        properPath = "library/static/library/{}.jpg".format(self.slug) #path for pathlib.Page
        staticPath = "library/{}.jpg".format(self.slug)                #path for static url
        image = Path(properPath)
        if image.is_file(): #if book has its image in /static/
            return staticPath
        else:
             return "library/defaultAuthor.jpg" #return default image for books
    
class Category(models.Model):
    class Meta:
        ordering = ['name']
    
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31, unique=True)
    
    def get_absolute_url(self):
        return reverse('library_category_detail', kwargs={'slug': self.slug})
        
    def get_delete_url(self):
        return reverse('library_delete_category', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('library_update_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
        
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Book(models.Model):
    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11,)
    description = models.TextField(default='')
    pages = models.PositiveSmallIntegerField()
    
    def get_absolute_url(self):
        return reverse('library_book_detail', kwargs={'slug': self.slug})
        
    def get_delete_url(self):
        return reverse('library_delete_book', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('library_update_book', kwargs={'slug': self.slug})   
        
    def get_img_path(self):
        properPath = "library/static/library/{}.jpg".format(self.slug) #path for pathlib.Page
        staticPath = "library/{}.jpg".format(self.slug)                #path for static url
        image = Path(properPath)
        if image.is_file(): #if book has its image in /static/
            return staticPath
        else:
             return "library/defaultBook.jpg" #return default image for books
    
    def printCategories(self):
        categories = ''
        query = self.category.all()
        for c in query:
            categories += c.name.title()
            if c != query.last():
                categories += ", "
        return categories
    
    def printAuthors(self):
        authors = ''
        query = self.authors.all()
        for a in query:
            authors += a.fullName()
            if a != query.last():
                authors += ", "
        return authors    
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Book.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
    
    def __str__(self):
        return self.title
        

    
    

    
 
