''' Imports '''
import random
import sys
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .forms import CommentForm, AddpostForm
from .models import Post, Comment, Feedback
from django.contrib import messages


class HomePage(generic.ListView):
    ''' Render home page'''

    model = Post
    queryset = Post.objects.filter(
            status=1, type="Post").order_by('-created_on')
    template_name = "index.html"
    posts = list(queryset)
    random_post = random.choice(posts)

    def get_context_data(self, **kwargs):
        ''' Ger random post if size not bigger than 200 char'''
        context = super(HomePage, self).get_context_data(**kwargs)
        context['random_post'] = self.random_post

        if sys.getsizeof(self.random_post) < 48.4:
            return context
        else:
            return HomePage()

        return render("index.html", context)


class PostsList(generic.ListView):
    ''' Different types of posts in posts.html'''
    model = Post
    queryset = Post.objects.all()
    template_name = "posts.html"

    def get_queryset(self):
        ''' Render triggered type using post_type'''
        queryset = super().get_queryset()
        new_qs = queryset.filter(type=self.kwargs['post_type'])
        return new_qs


class PostDetail(View):
    ''' Post related views'''
    model = Post
    template_name = 'post_detail.html'

    def get(self, request, slug):
        ''' Render separate post using slug'''
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, "post_detail.html",
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
            request, "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class Addpost(CreateView):
    ''' Add post '''
    model = Post
    template_name = "add_post.html"
    fields = ('title', 'status', 'slug', 'author', 'type', 'content')


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


class Feedback(CreateView):
    ''' Render contact.html '''
    model = Feedback
    template_name = "contact.html"
    fields = ('name', 'email', 'body')

    def contact(self, request):
        ''' Render contact.html '''
        return render(request, "contact.html")
