import undetected_chromedriver as uc
import time

# Start Chrome with undetected_chromedriver
options = uc.ChromeOptions()
options.headless = False  # Set to True if you want headless mode
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)

try:
    url = "https://www.realestate.com.au/agency/tag-real-estate-victoria-WKHCSZ"
    driver.get(url)

    # Wait for JavaScript challenge to complete
    time.sleep(10)  

    # Get the page source
    print(driver.page_source)

finally:
    driver.quit()
