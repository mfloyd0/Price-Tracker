from TrackerInterface import ITracker
import requests
from bs4 import BeautifulSoup
import pandas as pd


class BestBuy(ITracker):

    def track_price(self, product):
        print("Getting price from Best Buy")
        try:
            item = self.fetch_price(product["URL"])
        except:
            print("error getting page.")
            return None


        item_update = self.process(item, product)

        if item_update != None:
            self.update_price_excel(item_update)

    def fetch_price(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}

        try:
            response = requests.get(url, headers=headers, timeout=20)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract product name and price
        product_name = soup.find("h1", class_="product-title").text.strip()
        price_element = soup.find("div", class_="price-current")
        if price_element:
            price = price_element.text.strip()
            # Clean price by removing non-numeric characters
            cleaned_price = float(price.replace("$", "").replace(",", ""))
            return {"name": product_name, "Price": cleaned_price}
        else:
            print("Price not found on the page.")
            return None

    def process(self, current, lastChecked):

        print(current["Price"])
        print(lastChecked["Price"])
        if current["Price"] != lastChecked["Price"]:
            if lastChecked["Price"] > current["Price"]:
                print("sale")
                print("send notification")
                lastChecked["Price"] = current["Price"]
                if lastChecked["Lowest Recorded"] != lastChecked["Lowest Recorded"]:  # for empty cell
                    lastChecked["Lowest Recorded"] = current["Price"]

                return lastChecked

        else:
            print("no change")
            return None

    def update_price_excel(self, update):
        df = pd.read_excel('products to track.xlsx')

        for index, row in df.iterrows():
            if update["URL"] == row['URL']:
                df.loc[df["URL"] == update["URL"], "Price"] = update["Price"]
                df.to_excel('products to track.xlsx', index=False)
                print("price updated")

