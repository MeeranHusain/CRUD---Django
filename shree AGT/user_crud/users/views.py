from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

def index(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.hobbies = ", ".join(form.cleaned_data['hobbies'])
            user.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'users/form.html', {'form': form})

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.hobbies = ", ".join(form.cleaned_data['hobbies'])
            user.save()
            return redirect('index')
    else:
        form = UserForm(instance=user)
        form.initial['hobbies'] = user.hobbies.split(", ")
    return render(request, 'users/form.html', {'form': form})

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('index')
