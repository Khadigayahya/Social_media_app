from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from posts.models import Post
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form})

from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Comment

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

