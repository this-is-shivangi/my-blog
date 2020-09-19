from django.shortcuts import get_object_or_404,render
from .models import Post
from django.utils import timezone


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'home.html',{"posts":posts})

def post_details(request):
    post = get_object_or_404(Post)
    return render(request, 'details.html',{'post':post})

def log(request):
    return render(request,'login.html',{})


def sign(request):
    return render(request,'signup.html',{})

def about(request):
    return render(request,'about.html',{})

