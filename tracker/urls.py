from django.urls import path
from .views import UserCreate, UpdateUserProfile, UserProfile

urlpatterns = [
    path('user_registration/', UserCreate.as_view(), name='user_create'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='user_profile'),
    path('update_profile/<int:pk>/', UpdateUserProfile.as_view(), name='profile_update'),
]
