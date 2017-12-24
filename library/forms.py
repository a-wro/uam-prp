from django.forms import ModelForm
from .models import Book, Category
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
    def clean_title(self):
        return self.cleaned_data['title'].title()
        
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
        
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
    def clean_name(self):
        return self.cleaned_data['name'].lower()
        
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
