from selenium import webdriver
import os

class FindbyLinkText():

    def test(self):

        baseURL = "/Users/nikhilraobalaji/PycharmProjects/SeleniumWebdriver-Python/PythonTutorials/chromedriver"
        os.environ["webdriver.chrome.driver"] = baseURL
        driver = webdriver.Chrome(baseURL)

        practicePage = driver.find_element_by_link_text("Practice Page")

        if practicePage:
            print ("We have a Link Text")


ff = FindbyLinkText()
ff.test()
