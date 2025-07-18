from django.shortcuts import render 
from blog.models import Post


def index(request):
    Posts = Post.objects.all()
    return render(request,'website/index.html',{'posts': Posts})


    
