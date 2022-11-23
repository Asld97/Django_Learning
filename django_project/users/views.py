from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm -> Django default form
from django.contrib import messages
# Personalized form which inherit from UserCreationForm
from .forms import UserRegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to Log In!')
            return redirect('login')
    else:
        form = UserRegisterForm

    return render(request, 'users/register.html', {'form': form})
