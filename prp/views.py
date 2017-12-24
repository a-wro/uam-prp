from django.shortcuts import redirect
from django.urls import reverse

def redirect_root(request):
    urlpath = reverse('library_book_list')
    return redirect(urlpath)
    

    
    
    

    
