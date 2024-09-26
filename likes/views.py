from django.shortcuts import render
# likes/views.py

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post
from comments.models import Comment
from .models import Like

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('post_detail', pk=post.id)

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like, created = Like.objects.get_or_create(user=request.user, comment=comment)
    if not created:
        like.delete()
    return redirect('post_detail', pk=comment.post.id)

