from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bag_index(request):
    return render(request, 'bags/index.html', {'bags': bags})


class Bag:
    def __init__(self, brand, name, color, texture, description):
        self.brand = brand
        self.name = name
        self.color = color
        self.texture = texture
        self.description = description
        
bags = [
    Bag('Dior', 'Mini Lady', 'Cherry Red', 'Patent Cannage Calfskin', 'Epitomizes elegance & beauty'),
    Bag('Chanel', 'Small Flap Bag', 'Light Yellow', 'Shiny Lambskin', 'Spring & Summer 2025 pre-collection'),
    Bag('Gucci', 'Small GG Marmont Shoulder Bag', 'Black Matelassé', 'Chevron Leather', 'Adjustable chain shoulder strap'),
    Bag('YSL', 'Calypso Small', 'Vert Emeraude', 'Jacquard', 'Supple bag in baroque floral jacquard'),
    
]
        

        

