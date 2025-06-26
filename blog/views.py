from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import CommentForm, AuthorForm, PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def posts_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'blog/posts_by_author.html', {'author': author, 'posts': posts})


def create_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('author_list')
    return render(request, 'blog/create_author.html', {'form': form})

def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blog/create_post.html', {'form': form})

def create_comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blog/create_comment.html', {'form': form})
