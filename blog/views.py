from django.shortcuts import render, HttpResponseRedirect, Http404
from django.views.generic import ListView

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from django import forms
from .forms import Signupform,LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import Group
from .models import Post
from django.views.generic.list import ListView
from pprint import  pprint

# Create your views here.
def  index(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html', {'posts':posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        user = request.user.username
        if user == 'admin':
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(author=user)

        return render(request, 'blog/dashboard.html',{'posts': posts, 'user': user})
    else:
        return HttpResponseRedirect('/blog/login')

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
                    return HttpResponseRedirect('/blog/dashboard/')
                else:
                    messages.warning(request, "Something went wrong")
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/blog/dashboard/')

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

    return HttpResponseRedirect('/blog/login')

def create_post(request):
    if request.user.is_authenticated:        
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                subtext = form.cleaned_data['subtext']
                desc = form.cleaned_data['desc']
                author = request.user.username

                post = Post(title = title, subtext = subtext, desc = desc, author = author)
                post.save()
                form = PostForm()             
              
                messages.success(request, 'Congratulations! your post has been saved')

            else:
                messages.warning(request, 'Something went wrong')
                form = PostForm()
        else:
            form = PostForm() #if GET

        return render(request, 'blog/create_post.html', {'form': form})
    else:
        return HttpResponseRedirect('/blog/login')

def edit_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(pk=id)
            form = PostForm(request.POST or None, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,"Updated!!")
                return render('blog/dashboard.html/')
        else:
            post = Post.objects.get(pk = id)
            form = PostForm(request.POST, instance = post)
        return  render(request, 'blog/edit_post.html',{'form' : form } )
    else:
        return HttpResponseRedirect('blog/login/')


def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(pk=id)
            if post.delete() :
                return HttpResponseRedirect('/blog/dashboard/')
            else:
                return Http404()
    else:
        return HttpResponseRedirect('/blog/login/')
# class PostListView(generic.ListView):
#     model = Post
#     paginate_by = 10