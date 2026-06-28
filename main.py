import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time
from urllib.parse import urlparse, urlsplit


def fetch_price(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
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
        return {"name": product_name, "price": cleaned_price}
    else:
        print("Price not found on the page.")
        return None


def calculate(current, lastChecked):

    if current["price"] != lastChecked["Last Price"]:
        if lastChecked["Last Price"] > current["price"]:
            print("sale")
            print("send notification")
            if lastChecked["Lowest Recorded"] != current[ "Lowest Recorded"]: #for empty cell
                lastChecked["Lowest Recorded"] = current["price"]
                return lastChecked

    else:
        print("Price same")
        return lastChecked




if __name__ == "__main__":

    df = pd.read_excel('products to track.xlsx')

    # Loop through rows
    for index, row in df.iterrows():
        # print(f"Index: {index}, Website Name: {row['Website Name']}, Name: {row['Name']}")

        product = {
            "Website Name": row['Website Name'],
            "Name": row['Name'],
            "URL": row['URL'],
            "Last Price": row['Last Price'],
            "Lowest Recorded": row['Lowest Recorded'],
        }

        url = row['URL']

        # Extract the full hostname string
        hostname = urlsplit(url).hostname


        product_info = fetch_price(url)

        updated_info = calculate(product_info, product)






