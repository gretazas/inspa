from django.shortcuts import render, get_object_or_404, reverse
from .models import Post
from django.views import generic, View
from .forms import CommentForm
from django.http import HttpResponseRedirect
import random


class homePage(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"


class AllPostsList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "posts.html"


# def random_post(request):
#     post_ids = Post.objects.all().values_list('slug', flat=True) 
#     random_obj = Post.objects.get(post_id=random.choice(post_ids))
#     context = {
#         'random_post': random_obj,
#         }
#     return render(request, 'index.html', context)

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))



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
