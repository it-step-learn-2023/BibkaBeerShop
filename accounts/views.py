from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def profile(request):
    return render(request, 'accounts/profile.html', context={
        'title' : 'Профіль'
    })

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_in.html', context={
            'title' : 'Вхід',
            'page': 'sign in',
            'app' : 'accounts' 
        })
    else:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        user = authenticate(request, username=login_x, password=pass1_x)

        message = 'report message'
        color = 'report color'
        #
        if user is None:
            message = 'Користувач не знайденний! Перевірте Логін або пароль!'
            color = 'red'
            return render(request, 'accounts/reports.html', context={
                'title' : 'Звіт',
                'message' : message,
                'color' : color,
                'page': 'report',
                'app' : 'accounts'                
            })
        else:
            login(request, user)
            return redirect('/home')

def sign_out(request):
    logout(request)
    return redirect('/')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_up.html', context={
            'title' : 'Реєстрація',
            'page': 'Sign up',
            'app' : 'accounts'
        })
    else:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        email_x = request.POST.get('email')

        try:
            user = User.objects.create_user(login_x, email_x, pass1_x) 
            user.save()
        except:
            return redirect('/accounts/error')

        message = 'report message'
        color = 'report color'

        if user is None:
            message = 'В реєстраціі відмовлено!'
            color = 'red'
        else:
            message = 'Успішна реєестрація'
            color = 'green'

        return render(request, 'accounts/reports.html', context={
            'title' : 'Сторінка звіту',
            'message' : message,
            'color' : color,
            'page': 'report',
            'app' : 'accounts' 
        })

def error(request):
    return render(request, 'accounts/error.html', context={
        'title' : 'Помилка логіна або емаіла',
        'page': 'error',
        'app' : 'accounts'
    })