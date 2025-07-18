from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post

    
def blog_detail(request, slug):
   post = get_object_or_404(Post, slug=slug)
   return render(request, 'blog/blog_detail.html',{'post':post})

    



