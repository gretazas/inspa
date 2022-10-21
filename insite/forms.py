''' Imports '''
from .models import Comment, Post, Feedback
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
        fields = ('title',)


class AddFeedback(forms.ModelForm):
    class Meta:
        ''' Meta '''
        model = Feedback
        fields = ('name', 'email', 'body')
        # wiglets = {
        #     'name': forms.CharField(atts={'class': 'form-control'}),
        #     'email': forms.EmailField(atts={'class': 'form-control'}),
        #     'body': forms.EmailField(atts={'class': 'form-control'}),
        # }
