from django.shortcuts import render, HttpResponseRedirect, Http404

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from django import forms
from .forms import Signupform,LoginForm
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from .models import Post

# Create your views here.
def  index(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html', {'posts':posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    return render(request, 'blog/dashboard.html')

def user_login(request):    
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request = request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=name, password = password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login was successful")
                    return HttpResponseRedirect('/blogs/dashboard')
                else:
                    messages.warning(request, "Something went wrong")
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/blogs/dashboard')
    # form = LoginForm()
   # return render(request, 'blog/login.html', {'form': form})


def user_signup(request):
    if request.method == "POST" :
        form = Signupform(request.POST)
        if form.is_valid():
            messages.success(request, "Successfuly created user ")
            form.save()
            
    else:
        form = Signupform()
    return render(request, 'blog/signup.html', { 'form': form })

def user_logout(request):
   
    logout(request)

    return HttpResponseRedirect('/blogs/login')