from django.urls import path

from .views import IndexView

app_name = 'app_jobs'


urlpatterns = [
    path('', IndexView.as_view(), name='index')
]