from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import myblogs

# Create your views here.



def ablog(request):
    blogs = myblogs.objects.order_by('-date')
    return render(request,'blog.html', {'blogs' : blogs})


def detail(request,blog_id):
    blog = get_object_or_404(myblogs, pk=blog_id)
    return render(request, 'ind_blog.html', {'blog' : blog})
