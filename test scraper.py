import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sitetrackers import bestbuy


def fetch_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }

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


def item_Check(link):
    status = False
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Emulation.setUserAgentOverride', {

        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",

        "platform": "Win32",

        "acceptLanguage": "ro-RO"

    })

    driver.get(link)
    try:
        titleSection = driver.find_element(By.CSS_SELECTOR, "[data-component-name='ProductHeader']")
        print(titleSection.text)

    except NoSuchElementException:
        print("element not found")
    except TimeoutException:
        print("timeout error")
    except:
        print("error")
    finally:
        driver.close()
        driver.quit()

    return status



if __name__ == "__main__":

    bot_checker = "https://bot.sannysoft.com/"

    bestbuy = "https://www.bestbuy.com/product/msi-nvidia-geforce-rtx-5080-16g-gaming-trio-oc-16gb-gddr7-pci-express-gen-5-graphics-card-black/J3P7TX6L24"


    item_Check(bestbuy)

    # fetch_price("https://www.bestbuy.com/product/msi-nvidia-geforce-rtx-5080-16g-gaming-trio-oc-16gb-gddr7-pci-express-gen-5-graphics-card-black/J3P7TX6L24")