from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView

from app_users.models import User
from app_jobs.models import Vacancy
from .forms import HomePageForm


class IndexView(FormView):
    form_class = HomePageForm
    template_name = 'app_jobs/index.html'

    def get_success_url(self):
        return reverse_lazy('app_jobs:search_result', args=(1,))


class SearchResultView(ListView):
    model = Vacancy
    template_name = 'app_jobs/search_result.html'
    context_object_name = 'vacancy_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(city_name=self.request.user.city, language=self.request.user.language)
        return queryset.filter(city_name=self.request.GET['city'], language=self.request.GET['language'])






