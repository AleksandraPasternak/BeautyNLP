import json
from bs4 import BeautifulSoup
import requests
import pandas as pd


class ProductScrapper:
    def __init__(self):
        self.price_categories = []
        self.products_list = []
        self.prices = []
        self.url = ''

    def search_for_products(self):
        under_fifty = 'price%5B%5D=Poni%C5%BCej+50%2C00+z%C5%82'
        over_hundred = 'price%5B%5D=50%2C00+z%C5%82+-+100%2C00+z%C5%82&price%5B%5D=100%2C00+z%C5%82+-+150%2C00+z%C5%82&price%5B%5D=150%2C00+z%C5%82+-+250%2C00+z%C5%82&price%5B%5D=250%2C00+z%C5%82+lub+wi%C4%99cej'

        self.price_categories.append(under_fifty)
        self.price_categories.append(over_hundred)
        [self.search_in_price_category(cat) for cat in self.price_categories]

        self.save_results()

    def search_in_price_category(self, price_des):
        index = self.price_categories.index(price_des)
        last_page = 10 if index == 0 else 11
        for i in range(1, last_page):
            self.url = 'https://jejustore.pl/t/rodzaj/twarz?page=' + str(i) + '&' + price_des + '&sort='
            self.add_product(index)

        last_page = 9 if index == 0 else 4
        for i in range(1, last_page):
            self.url = 'https://jejustore.pl/t/rodzaj/cialo?page=' + str(i) + '&' + price_des + '&sort='
            self.add_product(index)

        last_page = 4 if index == 0 else 2
        for i in range(1, last_page):
            self.url = 'https://jejustore.pl/t/rodzaj/wlosy?page=' + str(i) + '&' + price_des + '&sort='
            self.add_product(index)

        last_page = 3 if index == 0 else 6
        for i in range(1, last_page):
            self.url = 'https://jejustore.pl/t/rodzaj/makijaz?page=' + str(i) + '&' + price_des + '&sort='
            self.add_product(index)

        last_page = 3 if index == 0 else 6
        for i in range(1, last_page):
            self.url = 'https://jejustore.pl/t/rodzaj/makijaz?page=' + str(i) + '&' + price_des + '&sort='
            self.add_product(index)

        last_page = 4 if index == 0 else 2
        for i in range(1, last_page):
            self.url = 'https://jejustore.pl/t/rodzaj/dlonie-slash-stopy-slash-paznokcie?page=' + str(
                i) + '&' + price_des + '&sort='
            self.add_product(index)

        self.url = 'https://jejustore.pl/t/rodzaj/dermokosmetyki?' + price_des + '&sort='
        self.add_product(index)

        if index == 0:
            self.products_list = self.products_list[:1268]
            self.prices = self.prices[:1268]

    def add_product(self, price_cat):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id='content')
        rows = results.find_all('div', class_='row')

        for row in rows:
            products = row.find_all('div', class_='col-12 col-sm-5ths')
            for product in products:
                data = product.find('product-card-container')['product']
                data_json = json.loads(data)
                self.products_list.append(data_json['data']['attributes']['description'])
                self.prices.append(price_cat)

    def save_results(self):
        df = pd.DataFrame({'Product Description': self.products_list, 'Price Category': self.prices})
        df.to_csv('products.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    product_scrapper = ProductScrapper()
    product_scrapper.search_for_products()
