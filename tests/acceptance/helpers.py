from selenium import webdriver

SELENIUM_HOST = 'selenium.local'
BASE_URL = 'http://myapp-flask-1'
driver = None

def get_driver():
    global driver
    cap = webdriver.common.desired_capabilities.DesiredCapabilities.CHROME
    url = 'http://'+SELENIUM_HOST+':4444/wd/hub'
    driver = webdriver.remote.webdriver.WebDriver(url, cap)
    return driver

def login():
    driver.get(BASE_URL)
    emailElem = driver.find_element_by_name("username")
    emailElem.send_keys("test123")
    passwordElem = driver.find_element_by_name("password")
    passwordElem.send_keys("test123")
    driver.find_element_by_xpath("//input[@value='Log In']").click()
    button.click()

