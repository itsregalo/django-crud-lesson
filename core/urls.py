from django.urls import path
from .views import IndexView, DetailView, CreateView

app_name = 'core'

urlpatterns = [
    path('', IndexView, name='index'),
    path('detail/<int:pk>/', DetailView, name='post-detail'),
    path('upload/', CreateView, name='post-create')
]
