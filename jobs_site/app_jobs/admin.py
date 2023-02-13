from django.contrib import admin

from .models import City, Language, Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'company_name', 'city_name')
    list_display_links = ('title', 'link', 'company_name')
    search_fields = ('title', 'company_name')
    list_filter = ('city_name', 'language')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_for_habr', 'id_for_hh')
    search_fields = ('name',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Language, LanguageAdmin)
