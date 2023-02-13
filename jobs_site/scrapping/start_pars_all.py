import itertools
import os
import sys
from typing import Dict, List

import django
from requests import Response

# Запускаем настройки django для обращения к БД
project_path = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'jobs_site.settings'
django.setup()

from http import HTTPStatus

import requests
from django.db import DatabaseError
from fake_useragent import UserAgent
from parser_habr import run_parser_habr
from parser_hh_ru import run_parser_hh
from progress.bar import IncrementalBar

from app_jobs.models import City, Language, Vacancy


def get_request(url: str) -> Response | bool:
    """Get-запрос по url"""

    rand_user_agent = UserAgent().random
    params = {
        "User-Agent": rand_user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    response = requests.get(url, params=params)

    if response.status_code == HTTPStatus.OK:
        return response
    return False


def add_in_db(language: str, city_name: str, data: List[Dict]) -> None:
    """Добавление вакансии в БД"""

    try:
        for vacancy_data in data:
            Vacancy.objects.create(
                **vacancy_data,
                city_name=city_name,
                language=language
            )
    except DatabaseError:
        pass


def main(language: str, city_name: str) -> None:
    """Получение города из БД и парсинг вакансий"""

    city = City.objects.get(name=city_name.lower())
    city_id_habr = city.id_for_habr
    city_id_hh = city.id_for_hh
    response_data = get_request(
        url=f'https://career.habr.com/vacancies?locations[]={city_id_habr}&q={language}&type=suitable'
    )
    if response_data:
        habr_jobs = run_parser_habr(response_data)
        add_in_db(language=language, city_name=city_name, data=habr_jobs)

    response_data = get_request(
        url=f'https://api.hh.ru/vacancies/?enable_snippets=true&ored_clusters=true&text='
            f'{language}&order_by=relevance&area={city_id_hh}')
    if response_data:
        hh_jobs = run_parser_hh(response_data.json())
        add_in_db(language=language, city_name=city_name, data=hh_jobs)


def fill_database():
    """Наполнение БД по комбинациям город+язык программирования"""

    cities = City.objects.all()
    languages = Language.objects.all()
    combinations_data = list(itertools.product(cities, languages))
    print(f'Найдено: {len(combinations_data)} комбинаций')

    # статус бар
    bar = IncrementalBar('Countdown', max=len(combinations_data))
    for combination in combinations_data:
        bar.next()
        main(language=combination[1].name, city_name=combination[0].name)

    bar.finish()


if __name__ == '__main__':
    fill_database()
