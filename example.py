from selenium import webdriver
from selenium.webdriver.common import keys

@test
def example_test():
    d = webdriver.Chrome()
    cookie={
        "name":"welcome",
        'value':"True",
        "expires": "",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': True
    }
    # d.add_cookie(cookie_dict=cookie)
    d.get("https://automationintesting.online/#/admin")
    d.find_element_by_css_selector("#next").click()
    d.find_element_by_css_selector("#next").click()
    d.find_element_by_css_selector("#next").click()
    d.find_element_by_css_selector("#next").click()
    d.find_element_by_css_selector("#closeModal").click()
    d.find_element_by_css_selector("#username").send_keys("admin")
    d.find_element_by_css_selector("#password").send_keys("password" + keys.Keys.ENTER)

    # d.quit()