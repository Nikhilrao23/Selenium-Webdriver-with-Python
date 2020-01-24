from selenium import webdriver
import os

class FindbyClassTag():

    def test(self):

        baseURL = "/Users/nikhilraobalaji/PycharmProjects/SeleniumWebdriver-Python/PythonTutorials/chromedriver"
        os.environ["webdriver.chrome.driver"] = baseURL
        driver = webdriver.Chrome(baseURL)

        driver.get("https://learn.letskodeit.com/p/practice")




ff = FindbyClassTag()
ff.test()
