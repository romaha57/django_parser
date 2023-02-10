from django.urls import path

from .views import IndexView, SearchResultView

app_name = 'app_jobs'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('result/<int:page>/', SearchResultView.as_view(), name='search_result'),
]
