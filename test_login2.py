import time


class Test_login2:
 def test_url2(self):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Edge()
    driver.get("https://amazon.com/")
    time.sleep(5)
