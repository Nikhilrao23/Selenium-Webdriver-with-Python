from selenium import webdriver
import os
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):

        baseURL = "/Users/nikhilraobalaji/PycharmProjects/SeleniumWebdriver-Python/PythonTutorials/chromedriver"
        os.environ["webdriver.chrome.driver"] = baseURL
        driver = webdriver.Chrome(baseURL)
        driver.implicitly_wait(15)


        driver.get("https://learn.letskodeit.com/p/practice")

        elementByID = driver.find_element(By.ID, "hondacheck")
        elementByID.click()

        if elementByID:
            print ("We found an element with ID")

        elementByXpath = driver.find_element(By.XPATH, "//option[@value = 'bmw']")
        elementByXpath.click()

        if elementByXpath:
            print ("We found an element by Xpath")

        elementbyCSS = driver.find_element(By.CSS_SELECTOR, "#hondacheck")
        elementbyCSS.click()

        if elementbyCSS:
            print ("We found an element by CSS")



ff = ByDemo()
ff.test()
