from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    client_ip = get_client_ip(request)
    posts = Post.objects.all()
    print(posts)
    context={
        'client_ip':client_ip,
        'posts':posts,
        'title':'Test'
        }
    print(context)
    return render(request,'blog/home.html',context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip