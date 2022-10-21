''' Imports '''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Feedback


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    ''' Admins post '''
    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    ''' Post comment '''
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        ''' Comment aproval status '''
        queryset.update(approved=True)


@admin.register(Feedback)
class Feedback(admin.ModelAdmin):
    ''' Post comment '''
    list_display = ('name', 'email', 'body')
    search_fields = ('name', 'email', 'body')
