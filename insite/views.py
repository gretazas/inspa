from django.shortcuts import render, get_object_or_404

from .models import Post
from django.views import generic, View


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

def PostDetail(request):
    return render(request, "post_detail.html")


def contact(request):
    return render(request, "contact.html")


def exercise(request):
    return render(request, "tips_of_the_day/exercise.html")


def health(request):
    return render(request, "tips_of_the_day/health.html")


def mindfulness(request):
    return render(request, "tips_of_the_day/mindfulness.html")


def wealth(request):
    return render(request, "tips_of_the_day/wealth.html")