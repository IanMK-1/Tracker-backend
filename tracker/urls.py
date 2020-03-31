from django.urls import path
from .views import UserCreate, UpdateUserProfile, UserProfile, CreateDevice, DeviceList, CreateGPS

urlpatterns = [
    path('user_registration/', UserCreate.as_view(), name='user_create'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='user_profile'),
    path('update_profile/<int:pk>/', UpdateUserProfile.as_view(), name='profile_update'),
    path('user/<int:pk>/add_device/', CreateDevice.as_view(), name='add_device'),
    path('user/<int:pk>/device_list/', DeviceList.as_view(), name='device_list'),
    path('tracker/<device_identifier>/<command>/<longitude>/<latitude>/', CreateGPS.as_view(), name='add_gps'),
]
