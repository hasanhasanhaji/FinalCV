from django.shortcuts import render , get_object_or_404
from .models import Post


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


# def single_view(request):
#     return render(request, 'blog/single.html')

# def single_view(request,pid):
#     return render(request, 'blog/single.html')

def single_view(request,pid):
    post = get_object_or_404(Post, pk=pid)
    
    # simple counted_view
    post.counted_view += 1
    post.save()
    
    # Previous and next posts (by ID or publish date)
    previous_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    
    
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request, 'blog/single.html',context)
