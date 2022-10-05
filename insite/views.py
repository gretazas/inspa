import random
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .forms import CommentForm
from .models import Post
import sys


class HomePage(generic.ListView):
    ''' Render home page'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    posts = list(Post.objects.filter(status=1))
    random_post = random.choice(posts)

    def get_context_data(self, **kwargs):
        ''' Ger random post if size not bigger than 200 char'''
        context = super(HomePage, self).get_context_data(**kwargs)
        context['random_post'] = self.random_post

        if sys.getsizeof(self.random_post) < 48.4:
            return context
        else:
            return HomePage()

class PostsList(generic.ListView):
    ''' Posts in posts.html'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "posts.html"


class HealthPostsList(generic.ListView):
    ''' Posts in health.html'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "tips_of_the_day/health.html"


class ExercisePostsList(generic.ListView):
    ''' Posts in exercise.html'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "tips_of_the_day/exercise.html"


class MindfulnessPostsList(generic.ListView):
    ''' Posts in mindfulness.html'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "tips_of_the_day/mindfulness.html"


class WealthPostsList(generic.ListView):
    ''' Posts in wealth.html'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "tips_of_the_day/wealth.html"


class PostDetail(View):
    ''' Post related views'''

    def get(self, request, slug):
        ''' Render separate post using slug in url '''
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

    def post(self, request, slug):
        ''' Comments attached to posts '''
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
    ''' Post and functions related with like views '''
    def post(self, request, slug):
        ''' Function: toggle between liked and unliked '''
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def contact(request):
    ''' Render contact.html '''
    return render(request, "contact.html")
