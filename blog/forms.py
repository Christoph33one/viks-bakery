from .models import Comment, Post
from django import forms


# comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'excerpt', 'content', 'featured_image']
