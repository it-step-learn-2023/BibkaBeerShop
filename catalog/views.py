from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import *

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    all_categorys = Category.objects.all()
    all_producers = Producer.objects.all()
    #
    paginator = Paginator(all_products, 9)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'catalog/index.html', context={
        'title': 'Катaлог',
        'page' : 'index',
        'app' : 'catalog',
        'all_products' : all_products,
        'all_categorys' : all_categorys,
        'all_producers' : all_producers,
        'select_products' : page_object        
    })

def singl_product(request, product_id):
    product1 = Product.objects.get(id=product_id)
    coments = Coment.objects.filter(product=product_id)
    count = len(coments)
    if request.method == 'GET':
        if count == 0:
            product1.rate = 5
        else:
            end_rate = 0
            for c in coments:
                end_rate += int(c.rate)
            product1.rate = end_rate // count
          
        return render(request, 'catalog/singl_product.html', context={
            'title' : product1.name,
            "page": 'singl_product',
            'app': 'catalog',
            'singl_product' : product1,
            'singl_comments': coments,
            'coment_count' : count,
        })
    elif request.method == "POST":
        
        c_name = request.POST.get('c-name')
        c_rate = request.POST.get('c-rate')
        c_text = request.POST.get('c-text')

        coment1 = Coment.objects.create(name=c_name, rate=c_rate, coment_text=c_text, product=product1)
        coment1.save()

        return redirect(f'/catalog/singl_product/{product_id}')

def beer(request):
    all_beer = Product.objects.filter(category=1)

    paginator = Paginator(all_beer, 9)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'catalog/beer.html', context={
        'title': 'Катaлог',
        'page' : 'beer',
        'app' : 'catalog',
        'all_beer': all_beer,
        'select_beer': page_object,
    })

def wine(request):
    all_wine = Product.objects.filter(category=3)

    paginator = Paginator(all_wine, 9)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'catalog/wine.html', context={
        'title': 'Катaлог',
        'page' : 'wine',
        'app' : 'catalog',
        'all_wine': all_wine,
        'select_wine': page_object,
    })

def sidr(request):
    all_sidr = Product.objects.filter(category=2)

    paginator = Paginator(all_sidr, 9)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'catalog/sidr.html', context={
        'title': 'Катaлог',
        'page' : 'sidr',
        'app' : 'catalog',
        'select_sidr': page_object,
    })

def zakys(request):
    all_zakys = Product.objects.filter(category=4)

    paginator = Paginator(all_zakys, 9)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'catalog/zakys.html', context={
        'title': 'Катaлог',
        'page' : 'zakys',
        'app' : 'catalog',
        'all_zakys': all_zakys,
        'select_zakys': page_object,
    })

def add_product(request):
    if request.method == 'GET':
        if request.user.username == 'superbiba':
            return render(request, 'catalog/add_product.html', context={
                'title': 'Додавання нового продукту',
                'page' : 'add_product',
                'app' : 'catalog',
                'form': ProductForm(),
            })
        else:
            return redirect('/')
    elif request.method == 'POST':
        filled_form = ProductForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/catalog')

def edit_product(request, product_id):
    product_edit = Product.objects.get(id=product_id)
    if request.method == 'GET':
        return render(request, 'catalog/edit_product.html', context={
            'title': f'Редагування продукту {product_edit.name}',
            'page' : 'edit_product',
            'app' : 'catalog',
            "product": product_edit,
            'form' : ProductForm2(instance=product_edit)
        })
    elif request.method == "POST":
        form = ProductForm2(request.POST)
        if form.is_valid():
            product_edit.name = form.cleaned_data.get('name')
            product_edit.about = form.cleaned_data.get('about')
            product_edit.category = form.cleaned_data.get('category')
            product_edit.quantitiy = form.cleaned_data.get('quantitiy')
            product_edit.displacement = form.cleaned_data.get('displacement')
            product_edit.price = form.cleaned_data.get('price')
            product_edit.save()
        return redirect('/catalog')

def ajax_del_product(request):
    response = dict()
    product_id = request.GET.get('product_id')
    del_order = Product.objects.get(id=product_id)
    del_order.delete()
    response['result'] = 'Товар був успішно видалений із каталога товарів!'
    return JsonResponse(response)
