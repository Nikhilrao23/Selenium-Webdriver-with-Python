from selenium import webdriver
import os

class FindbyXpathCss():

    def test(self):

        baseURL = "/Users/nikhilraobalaji/PycharmProjects/SeleniumWebdriver-Python/PythonTutorials/chromedriver"
        os.environ["webdriver.chrome.driver"] = baseURL
        driver = webdriver.Chrome(baseURL)

        driver.get("https://learn.letskodeit.com/p/practice")

        elementbyXpath = driver.find_element_by_xpath("//*[@id = 'name1234']")

        if elementbyXpath:
            print ("We found an element by Xpath")

        elementByCSS = driver.find_element_by_css_selector("#displayed-text")

        if elementByCSS:
            print ("We found an element with CSS Selector")

ff = FindbyXpathCss()
ff.test()
