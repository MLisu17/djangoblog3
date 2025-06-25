from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

#Stworzyliśmy funkcje która pobiera (request) i zwraca (return) wartość wywołaną innej funkcji (render) która złoży w całość nasz szablon HTML
def post_list(request):
    posts=Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request,'blog3/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog3/post_detail.html',{'post':post})