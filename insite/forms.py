''' Imports '''
from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    ''' Comment form '''
    class Meta:
        ''' Meta '''
        model = Comment
        fields = ('email', 'body',)


class AddpostForm(forms.ModelForm):
    ''' Add post form '''
    class Meta:
        ''' Meta '''
        model = Post
        fields = ('title', 'type', 'content')

