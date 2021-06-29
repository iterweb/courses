import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ('work', 'rabota', 'dou', 'djinni')

headers = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43"},
]


def work(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:
                div_list = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_list:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    company = 'No name'
                    logo = div.find('img')
                    if logo:
                        company = logo['alt']
                    jobs.append({
                        'title': title.text,
                        'url': domain + href,
                        'description': content,
                        'company': company,
                        'city_id': city,
                        'language_id': language,
                        })
            else:
                errors.append({
                    'url': url,
                    'title': 'div does not exists'
                })
        else:
            errors.append({
                    'url': url,
                    'title': 'page do not response'
                })
    
    return jobs, errors


def rabota(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://rabota.ua'

    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            new_jobs = soup.find('div', attrs={'class': 'f-vacancylist-newnotfound'})
            if not new_jobs:
                table = soup.find('table', id='ctl00_content_vacancyList_gridList')
                if table:
                    tr_list = table.find_all('tr', attrs={'id': True})
                    for tr in tr_list:
                        div = tr.find('div', attrs={'class': 'card-body'})
                        if div:
                            title = div.find('h2', attrs={'class': 'card-title'})
                            href = title.a['href']
                            content = div.find('div', attrs={'class': 'card-description'})
                            company = 'No name'
                            p = div.find('p', attrs={'class': 'company-name'})
                            if p:
                                company = p.a.text
                            jobs.append({
                                'title': title.text,
                                'url': domain + href,
                                'description': content.text,
                                'company': company,
                                'city_id': city,
                                'language_id': language,
                                })
                else:
                    errors.append({
                        'url': url,
                        'title': 'table does not exists'
                    })
            else:
                errors.append({
                    'url': url,
                    'title': 'page is empty'
                })
        else:
            errors.append({
                    'url': url,
                    'title': 'page do not response'
                })

    return jobs, errors


def dou(url, city=None, language=None):
    jobs = []
    errors = []

    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)]) 
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='vacancyListId')
            if main_div:
                li_list = main_div.find_all('li', attrs={'class': 'l-vacancy'})
                for li in li_list:
                    #if '__hot' not in li['class']:
                    title = li.find('div', attrs={'class': 'title'})
                    href = title.a['href']
                    cont = li.find('div', attrs={'class': 'sh-info'})
                    content = cont.text
                    company = 'No name'
                    a = title.find('a', attrs={'class': 'company'})
                    if a:
                        company = a.text
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content,
                        'company': company,
                        'city_id': city,
                        'language_id': language,
                        })
            else:
                errors.append({
                    'url': url,
                    'title': 'div does not exists'
                })
        else:
            errors.append({
                    'url': url,
                    'title': 'page do not response'
                })
    
    return jobs, errors


def djinni(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://djinni.co'

    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_ul = soup.find('ul', class_='list-jobs')
            if main_ul:
                li_list = main_ul.find_all('li', attrs={'class': 'list-jobs__item'})
                for li in li_list:
                    title = li.find('div', attrs={'class': 'list-jobs__title'})
                    href = title.a['href']
                    cont = li.find('div', attrs={'class': 'list-jobs__description'})
                    try:
                        content = cont.p.text
                    except AttributeError:
                        content = 'к этой вакансии описания нет!'
                    company = 'No name'
                    comp = li.find('div', attrs={'class': 'list-jobs__details__info'})
                    if comp:
                        company = comp.a.find_next("a").text
                    jobs.append({
                        'title': title.text,
                        'url': domain + href,
                        'description': content,
                        'company': company,
                        'city_id': city,
                        'language_id': language,
                        })
            else:
                errors.append({
                    'url': url,
                    'title': 'div does not exists'
                })
        else:
            errors.append({
                    'url': url,
                    'title': 'page do not response'
                })
    
    return jobs, errors


if __name__ == "__main__":
    url = 'https://djinni.co/jobs/keyword-python/kyiv/'
    jobs, errors = djinni(url)
    h = codecs.open('djinni.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()