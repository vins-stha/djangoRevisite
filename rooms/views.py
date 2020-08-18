from django.shortcuts import render, HttpResponseRedirect, Http404

# Create your views here.
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django import forms
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
# from .models import Room
from .forms import UserRegistrationForm
from .models import User


def create_list(request):
    if request.method == 'POST':
        fm = UserRegistrationForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            user = User(name=name, email=email, password=password)
            user.save()
            return HttpResponseRedirect('/')

    else:
        fm = UserRegistrationForm()

    userList = User.objects.all()
    return render(request, 'rooms/create.html', {'form' : fm, 'userList' : userList } )

def delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk = id)
        if (user.delete()):
            return HttpResponseRedirect('/')
        else:
            return Http404()

def edit(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)       
        form = UserRegistrationForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/')
        else:
            user = User.objects.get(pk=id)
            form = UserRegistrationForm(instance=user)
            
    
    return render(request,  'rooms/update.html', {'form':form })
        

    #     if fm.is_valid:
    #         fm.save()           
    # else:
    #     user = User.objects.get(pk=id)
    #     fm = UserRegistrationForm(instance=user)

    #return render(request, 'rooms/update.html', {'user' : user, 'form':fm })
            # return Http404



# class RoomForm(forms.ModelForm):
#     class Meta:
#         model = Room
#         fields = '__all__'

# class RoomList(View):
#     def get(self, request):
#         rooms = list(Room.objects.all().values())
#         data = dict()
#         data ['rooms'] = rooms

#         return JsonResponse(data)

# class RoomDetail(View):
#     def get(self, request, pk):
#         room = get_object_or_404(Room, pk = pk)
#         data = dict()
#         data['room'] = model_to_dict(room)
#         return JsonResponse(data)

# class RoomCreate(CreateView):
#     def post(self,request):
#         data = dict()
#         form = RoomForm(request.POST)
#         if(form.is_valid):
#             romm = form.save()
#             data['room'] = model_to_dict(room)
#         else:
#             data['error'] = 'form not valid!'
        
#         return JsonResponse(data)