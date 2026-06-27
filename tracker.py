import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time
from apscheduler.schedulers.blocking import BlockingScheduler


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
    price_element = soup.find("span", class_="price")
    if price_element:
        price = price_element.text.strip()
        # Clean price by removing non-numeric characters
        cleaned_price = float(price.replace("$", "").replace(",", ""))
        return {"name": product_name, "price": cleaned_price}
    else:
        print("Price not found on the page.")
        return None


def save_to_csv(product_data):
    df = pd.DataFrame([product_data])
    df.to_csv("product_prices.csv", mode="a", header=not pd.io.common.file_exists("product_prices.csv"),
              index=False)


def job():
    product_url = "https://example.com/product/123"
    product_data = fetch_price(product_url)
    if product_data:
        save_to_csv(product_data)
        print("Data saved successfully.")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', hours=1)  # Run every hour
    try:
        scheduler.start()
    except KeyboardInterrupt:
        print("Scheduler stopped.")