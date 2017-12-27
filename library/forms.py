from django.forms import ModelForm
from .models import Book, Category, Author
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'authors', 'category', 'price', 'pages', 'description')
        
    def clean_title(self):
        return self.cleaned_data['title'].title()
        
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
        
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
    def clean_name(self):
        return self.cleaned_data['name'].lower()
        
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
        
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'From', 'born', 'url', 'info')
        
    def clean_name(self):
        return self.cleaned_data['first_name'].lower()
        
    def clean_slug(self):
        return self.cleaned_data['last_name'].lower()
        
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
