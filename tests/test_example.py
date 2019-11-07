from selenium import webdriver
from selenium.webdriver.common import keys

def test_example(selenium):
    d = webdriver.Chrome()

    d.quit()