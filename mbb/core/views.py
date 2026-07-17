from django.shortcuts import render

# Create your views here.
"""Self Explaination: The logic here decides what happens when
someone visits a URL"""

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')