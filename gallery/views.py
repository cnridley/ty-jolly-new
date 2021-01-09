from django.shortcuts import render, reverse, redirect
from .models import Gallery
# Create your views here.

def gallery(request):
    """A view to return gallery page"""
    gallery = Gallery.objects.all()

    context = {
        'gallery': gallery,
    }
    return render(request, 'gallery.html', context)