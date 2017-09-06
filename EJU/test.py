from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'http://172.28.32.60:81/home/login'


def login():
    driver = webdriver.Chrome()
    driver.get(url)

    driver.find_element_by_id('companyNo').send_keys('220937')
    driver.find_element_by_id('btnNext').click()
    
    '''       try:
        driver = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password2")))
    except Exception:
        print "too many time"    '''

    driver.implicitly_wait(10)
    driver.find_element_by_id('password2').send_keys('1')
    driver.find_element_by_id('btnNext').click()

    driver.implicitly_wait(10)

    driver.find_element_by_id('username').send_keys('wallace007')
    driver.find_element_by_id('password').send_keys('1')
    driver.find_element_by_id('btnLogin').click()


login()