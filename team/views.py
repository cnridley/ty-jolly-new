from django.shortcuts import render

# Create your views here.

def team(request):
    """A view to return index page"""
    
    return render(request, 'team.html')