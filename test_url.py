import time



class Test_url:
    def test_url1(self):

        from selenium import webdriver
        from selenium.webdriver.common.by import By

        driver = webdriver.Edge()
        driver.get("https://facebook.com/")
        time.sleep(5)


    def test_url2(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        driver = webdriver.Edge()
        driver.get("https://amazon.com/")
        time.sleep(5)

    def test_url3(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        driver = webdriver.Edge()
        driver.get("https://flipkart.com/")
        time.sleep(5)



