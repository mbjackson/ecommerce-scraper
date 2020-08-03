import requests
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, sku):
        self.sku = sku

    def extract(self):
        product_info = dict()
        r = requests.get("https://shopdisney.com/{}.html".format(self.sku))
        if r.status_code == 200:
            html = BeautifulSoup(r.content, features="html.parser")
            product_info["title"] = html.find("h1", class_="product-name").text
            product_info["price"] = html.find("span", class_="value").text.strip()
            product_info["image"] = html.find("img", class_="thumbnail-carousel__target")["src"]
            product_info["description"] = html.find("p", class_="prod-header").text.strip()
            product_info["url"] = "https://www.shopdisney.com/{}".format(self.sku)
        return product_info
