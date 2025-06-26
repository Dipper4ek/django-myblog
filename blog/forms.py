from django import forms
from .models import Author, Post, Comment

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']  # Обираємо автора

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author_name', 'text']
