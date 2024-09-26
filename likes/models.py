# likes/models.py

from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post', 'comment')

    def __str__(self):
        if self.post:
            return f"{self.user.username} likes Post {self.post.id}"
        elif self.comment:
            return f"{self.user.username} likes Comment {self.comment.id}"

