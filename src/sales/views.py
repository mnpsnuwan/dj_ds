from django.shortcuts import render

# Create your views here.

def home_view(request):
    hello = 'Hello World from the view!'
    return render(request, 'sales/main.html', {'hello':hello})
 