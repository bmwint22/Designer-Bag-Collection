from django.shortcuts import render

from django.http import HttpResponse

from .models import Bag


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bag_index(request):
    bags = Bag.objects.all()
    return render(request, 'bags/index.html', {'bags': bags})




try:
    bag = Bag.objects.get(id=1)
except Bag.DoesNotExist:
    print("This bag does not exist!")

