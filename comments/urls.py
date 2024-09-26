# comments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:post_id>/', views.add_comment, name='add_comment'),
    path('<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    # يمكنكِ إضافة مسارات أخرى حسب الحاجة
]
