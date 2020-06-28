from selenium import webdriver

BASE_URL = 'http://myapp-flask-1'
driver = None

def get_driver():
    global driver
    opts = webdriver.ChromeOptions()
    opts.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=opts)
    return drive

def login():
    driver.get(BASE_URL)
    emailElem = driver.find_element_by_name("username")
    emailElem.send_keys("test123")
    passwordElem = driver.find_element_by_name("password")
    passwordElem.send_keys("test123")
    driver.find_element_by_xpath("//input[@value='Log In']").click()
    button.click()

