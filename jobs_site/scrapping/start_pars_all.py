import itertools
from progress.bar import IncrementalBar
import os
import sys
import django
from django.db import DatabaseError

project_path = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'jobs_site.settings'
django.setup()

import requests
from fake_useragent import UserAgent
from http import HTTPStatus
from parser_habr import run_parser_habr
from parser_hh_ru import run_parser_hh
from app_jobs.models import Vacancy, City, Language


def get_request(url):
    rand_user_agent = UserAgent().random
    params = {
        "User-Agent": rand_user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    response = requests.get(url, params=params)

    if response.status_code == HTTPStatus.OK:
        return response
    return False


def add_in_db(language, city_name, data):
    try:
        Vacancy.objects.bulk_create([Vacancy(**vacancy_data, city_name=city_name, language=language) for vacancy_data in data])
    except DatabaseError:
        pass


def main(language, city_name):
    city = City.objects.get(name=city_name.lower())
    city_id_habr = city.id_for_habr
    city_id_hh = city.id_for_hh
    response_data = get_request(url=f'https://career.habr.com/vacancies?locations[]={city_id_habr}&q={language}&type=suitable')
    if response_data:
        habr_jobs = run_parser_habr(response_data)
        add_in_db(language=language, city_name=city_name, data=habr_jobs)

    response_data = get_request(
        url=f'https://api.hh.ru/vacancies/?enable_snippets=true&ored_clusters=true&text={language}&order_by=relevance&area={city_id_hh}')
    if response_data:
        hh_jobs = run_parser_hh(response_data.json())
        add_in_db(language=language, city_name=city_name, data=hh_jobs)


def fill_database():
    cities = City.objects.all()
    languages = Language.objects.all()
    combinations_data = list(itertools.product(cities, languages))
    print(f'Найдено: {len(combinations_data)} комбинаций')
    bar = IncrementalBar('Countdown', max=len(combinations_data))

    bar.finish()
    for combination in combinations_data:
        bar.next()
        main(language=combination[1].name, city_name=combination[0].name)

    bar.finish()


if __name__ == '__main__':
    fill_database()

