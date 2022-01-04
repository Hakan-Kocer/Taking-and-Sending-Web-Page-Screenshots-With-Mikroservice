from selenium import webdriver

def screenshot_foto_to_base64(url):
    driver_path="model/chromedriver"

    browser=webdriver.Chrome(driver_path)

    if not url.startswith("https://") and not url.startswith("http://"):
        servicePath = "http://" + url
    else:
        servicePath = url
    browser.get(servicePath)
    scrshot_base64=browser.get_screenshot_as_base64()
    browser.quit()
    return scrshot_base64
