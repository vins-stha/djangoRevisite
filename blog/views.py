from django.shortcuts import render, HttpResponseRedirect, Http404

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from django import forms



# Create your views here.
def  index(request):
    return render(request,'blog/index.html')