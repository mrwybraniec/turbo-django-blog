from django.http import HttpRequest
from django.shortcuts import render

from .models import Post


# Create your views here.
def post_list(request: HttpRequest):
    posts = Post.objects.order_by("created_date")
    return render(request, "blog/post_list.html", {"posts": posts})
