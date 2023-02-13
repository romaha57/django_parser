from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from .forms import HomePageForm
from .models import Vacancy


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
            if self.request.user.city == 'россия':
                return queryset.filter(language=self.request.user.language)
            else:
                return queryset.filter(city_name=self.request.user.city, language=self.request.user.language)
        else:
            if self.request.GET['city'] == 'россия':
                return queryset.filter(language=self.request.GET['language'])
            else:
                return queryset.filter(city_name=self.request.GET['city'], language=self.request.GET['language'])
