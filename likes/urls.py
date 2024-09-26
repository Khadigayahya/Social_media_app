# likes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    # يمكنكِ إضافة مسارات أخرى حسب الحاجة
]
