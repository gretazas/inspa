''' Imports '''
from .models import Comment, Post, User, Feedback
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


class FeedbackForm(forms.ModelForm):
    '''Add feedback'''
    class Meta:
        ''' Meta '''
        model = Feedback
        fields = ('body',)
        widgets = {
                'body': forms.Textarea(attrs={'rows': 3, 'cols': 35, 'class': 'feedback-form'})
        }
