from django.shortcuts import render
from django.core.mail import send_mail
from catalog.models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    #
    best_prod = []
    for p in all_products:
        if p.sales >= 50:
            best_prod.append(p)
            
    paginator = Paginator(best_prod, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'home/index.html', context={
        'title': 'Головна',
        'page' : 'index',
        'app' : 'home',
        'all_products' : all_products,
        'best_products' : page_object        
    })

def about(request):
    return render(request, 'home/about.html', context={
        'title': 'Про сайт',
        'page' : 'about',
        'app' : 'home'
    })

def contacts(request):
    if request.method == 'GET':
        return render(request, 'home/contacts.html', context={
            'title': 'Контакти',
            'page' : 'contacts',
            'app' : 'home'
        })
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        title = f'Повідомлення від користувача {name} !'
        body = f"""
            <h1>Повідомлення від користувача {name}</h1>
            <h1>Email: {email}</h1>
            <hr />
            <h2 style="color: brown">За темою: {subject}</h2>
            <hr />
            <h3>{message}</h3>
            <hr />
        """

        success = send_mail(title, '', email, ['webshop.support@gamil.com'], fail_silently=False, html_message=body)
        if success:
            return render(request, 'home/norm.html', context={
                'title': 'Відправлено',
                'page' : 'thanks',
                'app' : 'home',
            })
        else:
            return render(request, 'home/fail.html', context={
                'title': 'Помилка поштового відправлення',
                'page' : 'fail',
                'app' : 'home',
            })
