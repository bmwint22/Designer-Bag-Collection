from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bag

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bag_index(request):
    bags = Bag.objects.all()
    return render(request, 'bags/index.html', {'bags': bags})

def bag_detail(request, bag_id):
    try:
        bag = Bag.objects.get(id=bag_id)
    except Bag.DoesNotExist:
        return HttpResponse("This bag does not exist!")  
    
    return render(request, 'bags/detail.html', {'bag': bag})
class BagCreate(CreateView):
    model = Bag
    fields = '__all__'
    success_url = '/bags/'

class BagUpdate(UpdateView):
    model = Bag
    fields = ['name', 'color', 'texture', 'description']
    success_url = '/bags/'  

class BagDelete(DeleteView):
    model = Bag
    success_url = '/bags/'
