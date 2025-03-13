from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello Designer Bags!</h1>')

def about(request):
    return render(request, 'about.html')


class Bag:
    def __init__(brand, name, color, texture, description):
        self.brand = brand
        self.name = name
        self.color = color
        self.texture = texture
        self.description = description
        

        

