from selenium import webdriver
import os

class FindbyLinkText():

    def test(self):

        baseURL = "/Users/nikhilraobalaji/PycharmProjects/SeleniumWebdriver-Python/PythonTutorials/chromedriver"
        os.environ["webdriver.chrome.driver"] = baseURL
        driver = webdriver.Chrome(baseURL)

        driver.get("https://learn.letskodeit.com/p/practice")

        loginText = driver.find_element_by_link_text("Login")

        if loginText:
            print ("We found a Login Text")

        practicePage = driver.find_element_by_partial_link_text("Practice")

        if practicePage:
            print ("We found a link with Partial link Text")



ff = FindbyLinkText()
ff.test()
