from selenium import webdriver
import os


class RunChromeTest():

    def test(self):

        driverLocation = "/Users/nikhilraobalaji/PycharmProjects/PythonTutorials/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)

        driver.get("https://www.google.com")

ff = RunChromeTest()
ff.test()

"""
Firefox
1. Install Geckodriver
2. driver = webdriver.Firefox(executable_path = " ")
3. driver.get("https://www.google.com")

"""