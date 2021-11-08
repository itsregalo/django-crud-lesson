from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from .models import Post
from .forms import PostForm
# Create your views here.

def IndexView(request):
    posts = Post.objects.all()
    data = {
        'posts':posts
    }
    return render(request, 'index.html', data)
#detailview

def DetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)

    data = {
        'post':post
    }
    return render(request, 'post-detail.html', data)

#createview

def CreateView(request):
    form = PostForm()
    if request.method == 'POST':  
        data_form = PostForm(request.POST or None) 
        if data_form.is_valid():
            data_form.save()

            data = {
                'data':Post.objects.all()
            }
            return render(request, 'index.html', data)
        form = PostForm()
        return render(request, 'post-form.html', {'form':form})
    data = {
        'form':form
    }
    return render(request, 'post-form.html', data)


#updateview


#deleteview

