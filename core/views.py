from django.shortcuts import render
from .models import Post
# Create your views here.

def IndexView(request):
    posts = Post.objects.all()
    data = {
        'posts':posts
    }
    return render(request, 'index.html', data)


#detailview
#createview
#updateview
#deleteview

