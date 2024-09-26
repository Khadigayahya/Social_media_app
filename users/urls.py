# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # مثال لمسار عرض الملف الشخصي
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    # يمكنكِ إضافة مسارات أخرى حسب الحاجة
]
