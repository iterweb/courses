import requests
import validators
from bs4 import BeautifulSoup
from db_writer import DataWriter


header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"}


class OlxParser(DataWriter):
    def __init__(self):
        super().__init__()
        self.url = self.get_url()
        self.titles = self.get_data()

    # ввод URL и проверка валидности
    def get_url(self):
        while True:
            url = input('Введите url: ')
            # url = 'https://www.olx.ua/transport/legkovye-avtomobili/'
            if validators.url(url):
                return url
            else:
                print('not valid')

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
                # проверка на дубли в Безе Данных
                if title not in self.titles:
                    # запись в Data Base
                    self.save_data(title, price, published)

    def main(self):
        self.parser(self.get_html(self.get_url()))


if __name__ == '__main__':
    app = OlxParser()
    app.main()
