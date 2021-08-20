import requests
from bs4 import BeautifulSoup
from .models import OlxAdvert



header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"}


class OlxParser:

    # получаем html страницы
    def get_html(self, url):
        r = requests.get(url, headers=header)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    # поиск объявлений
    def parser(self, soup):

        advert_class = {
            'fixed offers breakword offers--top redesigned': 'marginright5 link linkWithHash detailsLink linkWithHashPromoted',
            'fixed offers breakword redesigned': 'marginright5 link linkWithHash detailsLink'
        }

        for key, val in advert_class.items():
            table = soup.find('table', class_=key)
            for tr in table.find_all('tr', class_='wrap'):
                title = tr.find('a', class_=val).text.strip()
                price = tr.find('p', class_='price').text.strip()
                td = tr.find('td', class_='bottom-cell')
                published = td.find_all('small', class_='breadcrumb x-normal')[1].text.strip()

                data = {
                    'title': title,
                    'price': price,
                    'published': published
                }
                obj = OlxAdvert(**data)
                try:
                    obj.save()
                except:
                    pass

    def main(self, url):
        self.parser(self.get_html(url))
