from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html', context={
        'title': 'Каталог',
        'page' : 'index',
        'app' : 'catalog'
    })