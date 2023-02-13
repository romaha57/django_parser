from typing import Dict, List

from bs4 import BeautifulSoup as BS
from requests import Response


def run_parser_habr(response: Response) -> List[Dict]:
    """Собирает вакансии с сайта career.babr.com"""

    main_url = 'https://career.habr.com'
    jobs_data = []
    soup = BS(response.content, 'html.parser')
    vacancy_cards = soup.find_all('div', attrs={'class': 'vacancy-card'})

    for vacancy_card in vacancy_cards:
        date = vacancy_card.time['datetime']
        link = main_url + vacancy_card.a['href']
        logo = vacancy_card.img['src']
        company_name = vacancy_card.find('div', attrs={'class': 'vacancy-card__company-title'}).a.text
        title = vacancy_card.find('div', attrs={'class': 'vacancy-card__title'}).a.text
        meta_data = vacancy_card.find('div', attrs={'class': 'vacancy-card__meta'}).text
        salary = vacancy_card.find('div', attrs={'class': 'basic-salary'}).text
        if not salary:
            salary = 'зп не указана'
        requirements = vacancy_card.find('div', attrs={'class': 'vacancy-card__skills'}).text

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
