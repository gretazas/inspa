''' Imports '''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    ''' Post related items '''
    POST_TYPES = (
                ("Health", "Health"),
                ("Wealth", "Wealth"),
                ("Exercise", "Exercise"),
                ("Mindfulness", "Mindfulness")
                  )
    type = models.CharField(max_length=20, choices=POST_TYPES, default=None)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    exerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_like', blank=True)

    class Meta:
        ''' Meta '''
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        ''' Add post '''
        return reverse('')

    def number_of_likes(self):
        ''' The number of likes counted '''
        return self.likes.count()


class Comment(models.Model):
    ''' Comment section '''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ''' Meta '''
        ordering = ['created_on']

    def __str__(self):
        return f"Comment { self.body } by { self.name }"


class Feedback(models.Model):
    '''Feedback'''
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ''' Meta '''
        ordering = ['created_on']
