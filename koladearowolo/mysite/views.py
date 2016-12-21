from django.shortcuts import render
from . import views
from django.utils import timezone
from .models import Post

def index(request):
    return render(request, 'mysite/index.html', {})
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'mysite/blog.html', {'posts': posts})
# Create your views here.
