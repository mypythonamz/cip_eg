from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#item_link = "https://www.amazon.com/gp/product/B0CG9F5W3Q/ref=ox_sc_saved_image_2?smid=A3AGT0G8RH5ZSS&th=1"

def main():
    item_link = input("Please input link to amazon product: ")
    driver = webdriver.Chrome()  # path where chromedriver is located in docker environment
    driver.get(item_link)  # opens the actual chrome browser to navigate
    delay = 10
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-price-whole')))
    except TimeoutException:
        pass
    product = driver.find_element(By.XPATH, '//*[@id="productTitle"]')
    price_whole = driver.find_element(By.CLASS_NAME, 'a-price-whole')
    price_fraction = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
    price = "$"+price_whole.text+"."+price_fraction.text
    print("Loading price now!")
    print(f"Price of {product.text} is -->")
    print(price)



def set_chrome_options():
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--window-size=1920,1080')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}') # this option enabled it able to grab elements in headless mode
    chrome_prefs = {}
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    return chrome_options



if __name__ == '__main__':
    main()