from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            contributors = Group.objects.get(name='contributor')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.groups.add(contributors)
            login(request, user)
            return redirect('library_book_list')
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form})
