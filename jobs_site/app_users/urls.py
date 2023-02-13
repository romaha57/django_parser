from django.urls import path

from .views import ProfileView

app_name = 'app_users'

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
