import requests
from bs4 import BeautifulSoup

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.60'
    , 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_='ticket-item')

    cars = []
    if items == cars:
        """      парсинг для вантажівок    """
        items = soup.find_all('section', class_='proposition')
        for item in items:
            if item.find('span', class_='size22').get_text(strip=True) == "Ціну уточнюйте":
                cars.append({
                    'title': item.find('span', class_='link').get_text(strip=True),
                    'link': "https://auto.ria.com/uk" + item.find('a', class_='proposition_link').get('href'),
                    'usd_price': "Ціну уточнюйте!",
                    'ua_price': "Ціну уточнюйте!"
                })

            else:
                cars.append({
                    'title': item.find('span', class_='link').get_text(strip=True),
                    'link': "https://auto.ria.com/uk" + item.find('a', class_='proposition_link').get('href'),
                    'usd_price': item.find('span', class_='size22').get_text(strip=True),
                    'ua_price': item.find('span', class_='size16').get_text(strip=True)
                })
        return cars
    else:
        """  звичайний парсинг   """
        for item in items:
            cars.append({
                'title': item.find('div', class_='head-ticket').get_text(strip=True),
                'link': item.find('a', class_='m-link-ticket').get('href'),
                'usd_price': item.find('span', class_='bold green size22').get_text(strip=True),
                'ua_price': item.find('span', class_='i-block').get_text(strip=True)
            })
        return cars


def parse(URL):
    html = get_html(URL)
    if html.status_code == 200:
        cars = get_content(html.text)
        return cars
    else:
        print('Error')

# cars = parse("https://auto.ria.com/uk/newauto/search/?page=1&categoryId=6&order=1")
# for car in cars:
#    print(car)
