from selenium import webdriver
import os
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):

        baseURL = "/Users/nikhilraobalaji/PycharmProjects/SeleniumWebdriver-Python/PythonTutorials/chromedriver"
        os.environ["webdriver.chrome.driver"] = baseURL
        driver = webdriver.Chrome(baseURL)
        driver.implicitly_wait(15)


        driver.get("https://learn.letskodeit.com/p/practice")

        elementListByClassName = driver.find_elements(By.CLASS_NAME, "inputs")
        lengthClass = len(elementListByClassName)

        if elementListByClassName:
            print ("Size of the list is: " + str(lengthClass))

        elementListByTagName = driver.find_elements_by_tag_name("tr")
        lengthTag = len(elementListByTagName)


        if elementListByTagName:
            print ("Size of the list is: " +str(lengthTag))

ff = ListOfElements()
ff.test()
