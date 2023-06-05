from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.core.mail import send_mail
from .models import Order, Product

# Create your views here.
def index(request):
    return render(request, 'orders/index.html', {
        'title': 'Управління кошиком',
        'page' : 'index',
        'app' : 'orders',
        'user_orders' : Order.objects.filter(user_id=request.user.id),
    })

def ajax_cart(request):
    response = dict()
    response['test_message'] = 'AJAX work fine'
    
    # 1
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')
    cid = request.GET.get('cid')

    # 2
    try:
        Order.objects.create(
            code=f'Order-{pid}/{uid}',
            user_id=uid,
            product_id=pid,
            notes='Очікує підтвердження',
            count=cid
        )
    except:
        orderr = Order.objects.filter(user_id=uid)
        for orde in orderr:
            if orde.code == f'Order-{pid}/{uid}':
                orde.count += int(cid)
                orde.save()
    # 3
    count1 = 0
    total = 0
    user_orders = Order.objects.filter(user_id=uid)
    for order in user_orders:
        count1 += order.count
        total += order.product.price * order.count

    # 4
    response['count'] = count1
    response['total'] = total

    return JsonResponse(response)

def ajax_cart_display(request):
    response = dict()
    uid = request.GET.get('uid')
    user_orders = Order.objects.filter(user_id=uid)
    #
    count1 = 0    
    total = 0
    for order in user_orders:
        count1 += order.count
        total += order.product.price * order.count
    #
    response['count'] = count1
    response['total'] = total
    return JsonResponse(response)

def bill(request, sel_list: str):
    if request.method == 'GET':
        sel_list_str = sel_list.split(',')
        sel_list_num = [int(x) for x in sel_list_str[:-1]]
        total_price = int(sel_list_str[-1])
        final_list = []
        #
        for order_id in sel_list_num:
            order = Order.objects.get(id=order_id)
            final_list.append({
                'product_name': order.product.name,
                'category_name': order.product.category.name,
                'product_price': order.product.price,
                'product_photo': order.product.photo,
                'product_count': order.count,
            })
        #
        return render(request, 'orders/bill.html', context={
            'title': 'Оформлення рахунку',
            'page' : 'bill',
            'app' : 'orders',
            'total_price': total_price,
            'final_list': final_list,
            'init_list': sel_list,
        })
    
    elif request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')

        #
        sel_list_str = sel_list.split(',')
        sel_list_num = [int(x) for x in sel_list_str[:-1]]
        total_price = int(sel_list_str[-1])
        info_list = []
        #
        for order_id in sel_list_num:
            order = Order.objects.get(id=order_id)
            product = Product.objects.get(name=order.product.name)
            product.sales += int(order.count)
            product.save()
            if int(product.quantitiy) < int(order.count):
                product.quantitiy = 0
                product.save()
            else:
                product.quantitiy -= int(order.count)
                product.save()

            info_list.append({
                'product_name': order.product.name,
                'category_name': order.product.category.name,
                'product_price': order.product.price,
                'product_count': order.count
            })
            
            
        #
        subject = 'Повідомлення про замовлення на сайті WebShop'
        body = f"""
            <h1>Повідомлення про замовлення на сайті BibkaBeerShop UA</h1>
            <hr />
            <h2 style="color: brown">{surname} {name}, Ви підтвердили замовлення наступних товарів:</h2>
            <h3>
            <ol>
        """
        for item in info_list:
            body += f"""
                <li>{item['product_name']} / {item['category_name']} / {item['product_price']} грн - {item['product_count']} шт</li>
            """
        body += f"""
            </ol>
            </h3>
            <hr />
            <h2>Загальна сума до сплати: <span style="color: red;">{total_price} грн</span></h2>
            <h2 style="color: brown">Ваша адресса - {adress} / Номер телефону - {phone}</h2>
        """
        #
        success = send_mail(subject, '', 'bibkabeershop@ukr.net', [email], fail_silently=False, html_message=body)
        if success:
            return render(request, 'orders/thanks.html', context={
                'title': 'Подяка за замовлення',
                'page' : 'thanks',
                'app' : 'orders',
            })
        
        else:
            return render(request, 'orders/fail.html', context={
                'title': 'Помилка поштового відправлення',
                'page' : 'fail',
                'app' : 'orders',
            })

  

def ajax_del_order(request):
    response = dict()
    order_id = request.GET.get('order_id')
    del_order = Order.objects.get(id=order_id)
    del_order.delete()
    response['result'] = 'Товар був успішно видалений із кошика'
    return JsonResponse(response)

def ajax_cart_count(request):
    response = dict()
    response['test_message'] = 'AJAX work fine'
    
    # 1
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')
    cid = request.GET.get('cid')

    orderr = Order.objects.filter(user_id=uid)
    for orde in orderr:
        if orde.code == f'Order-{pid}/{uid}':
            orde.count = int(cid)
            orde.save()
    
    response['count'] = orde.count
    
        
    return JsonResponse(response)