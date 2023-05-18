from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def index(request):
    all_posts = Post.objects.all()
    #
    paginator = Paginator(all_posts, 2)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    #

    return render(request, 'blog/index.html', context={
        'title' : "Блог",
        "page": 'index',
        'app': 'blog',
        'select_posts' : page_object
    })

def singl_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/singl_post.html', context={
        'title' : post.title,
        "page": 'singl_post',
        'app': 'blog',
        'singl_post' : Post.objects.get(id=post_id)
    })
