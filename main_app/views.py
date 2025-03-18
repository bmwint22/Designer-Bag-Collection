from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bag
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    error_message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  
                return redirect('bag-index')  
            else:
                error_message = 'Invalid username or password'
        else:
            error_message = 'Invalid form submission'
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message})



class Home(LoginView):
    template_name = 'home.html'
    
def landing(request):
    return render(request, 'landing.html') 
    
@login_required
def bag_index(request):
    bags = Bag.objects.filter(user=request.user)
    return render(request, 'bags/index.html', {'bags': bags})

@login_required
def bag_detail(request, bag_id):
    try:
        bag = Bag.objects.get(id=bag_id)
    except Bag.DoesNotExist:
        return HttpResponse("This bag does not exist!")  
    
    return render(request, 'bags/detail.html', {'bag': bag})
class BagCreate(LoginRequiredMixin, CreateView):
    model = Bag
    fields = '__all__'
    success_url = '/bags/'
    
def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bag-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)



class BagUpdate(LoginRequiredMixin, UpdateView):
    model = Bag
    fields = ['name', 'color', 'texture', 'description']
    success_url = '/bags/'  

class BagDelete(LoginRequiredMixin, DeleteView):
    model = Bag
    success_url = '/bags/'
