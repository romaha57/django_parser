import pprint
import re

import requests


# def get_city_id(city_name):
#     city_name = city_name.lower()
#     response = requests.get('https://api.hh.ru/areas')
#     city_id = response.json()
#     pprint.pprint(city_id)
#     for i in city_id[0]["areas"]:
#         for j in i["areas"]:
#             if j["name"].lower() == city_name:
#                 return j['id']


# def formation_url_for_hh(language, city_name=None):
#    if city_name is None:
#        url = f"https://api.hh.ru/vacancies/?enable_snippets=true&ored_clusters=true&text={language}&order_by=relevance&area=113"
#    elif city_name.lower() == 'москва':
#       url = f"https://api.hh.ru/vacancies/?enable_snippets=true&ored_clusters=true&text={language}&order_by=relevance&area=1"
#    else:
#   #   city_id = get_city_id(city_name=city_name)
#       url = f"https://api.hh.ru/vacancies/?enable_snippets=true&ored_clusters=true&text={language}&order_by=relevance&area={city_id}"
#
#   return url


def run_parser_hh(response_data):
    jobs_data = []
    for vacancy in response_data['items']:
        date = vacancy['created_at']
        link = vacancy['alternate_url']
        logo_data = vacancy.get('employer').get('logo_urls')

        if not logo_data:
            logo = None
        else:
            logo = logo_data.get('90')
        company_name = vacancy['employer']['name']
        title = vacancy['name']
        meta_data = vacancy['schedule']['name']

        salary = vacancy.get('salary')

        if not salary:
            salary = 'зп не указана'
        else:
            salary_from = 0 if salary.get('from') is None else salary.get('from')
            salary_to = 0 if salary.get('to') is None else salary.get('to')
            salary = int((int(salary_from) + int(salary_to)) // 2)

        requirements = vacancy.get('snippet').get('requirement')
        if requirements:
            requirements = re.sub('<highlighttext>*', '', requirements)
            requirements = re.sub('</highlighttext>', '', requirements)

        jobs_data.append({
            'date': date,
            'link': link,
            'logo': logo,
            'company_name': company_name,
            'title': title,
            'meta_data': meta_data,
            'salary': salary,
            'requirements': requirements,
        })

    return jobs_data

