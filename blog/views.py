from django.shortcuts import render,reverse
from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from .models import Post


def blog_detail(request, id):
   post = get_object_or_404(Post, id=id)
   return render(request, 'blog/blog_detail.html', {'post': post,})

def like_post (request, pk ):
    post = Post.objects.get(pk=pk)
    post.likes += 1
    post.save()
    post.count = post.likes
    return HttpResponseRedirect(reverse("blog_detail", args=(post.id,)))

