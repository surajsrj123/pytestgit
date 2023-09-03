import time





class Test_login1:
    def test_login1(self):

        from selenium import webdriver
        from selenium.webdriver.common.by import By

        driver = webdriver.Edge()
        driver.get("https://facebook.com/")
        time.sleep(5)
        driver.find_element(By.ID,"email").send_keys("patilsuraj@gmail.com")
        driver.find_element(By.ID, "pass").send_keys("surajpatil")
        time.sleep(5)
