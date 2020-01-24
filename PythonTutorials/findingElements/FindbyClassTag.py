from selenium import webdriver
import os

from selenium.webdriver.common.by import By

class FindbyClassTag():

    def test(self):

        baseURL = "/Users/nikhilraobalaji/PycharmProjects/SeleniumWebdriver-Python/PythonTutorials/chromedriver"
        os.environ["webdriver.chrome.driver"] = baseURL
        driver = webdriver.Chrome(baseURL)

        driver.get("https://learn.letskodeit.com/p/practice")

        elementbyClassName = driver.find_element_by_class_name("displayed-class")
        elementbyClassName.send_keys("Nikhil is Testing")


        if elementbyClassName:
            print ("We found an element with Class Name")

        elementbyTagName = driver.find_element_by_tag_name("h1")
        text = elementbyTagName.text

        if elementbyTagName:
            print ("We found an element with Tag Name: "+ text)


ff = FindbyClassTag()
ff.test()
