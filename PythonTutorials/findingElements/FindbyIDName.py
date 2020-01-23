from selenium import webdriver
import os

class FindbyIDName():

    def test(self):

        baseURL = "/Users/nikhilraobalaji/PycharmProjects/SeleniumWebdriver-Python/PythonTutorials/chromedriver"
        os.environ["webdriver.chrome.driver"] = baseURL
        driver = webdriver.Chrome(baseURL)

        driver.get("https://learn.letskodeit.com/p/practice")

        elementByID = driver.find_element_by_id("benzradio")

        if elementByID:
            print ("We found an element by id")

        elementByName = driver.find_element_by_name("cars")

        if elementByName:
            print ("We found an element by Name - Cars")


ff = FindbyIDName()
ff.test()
